from fastapi import FastAPI,Request,Response,Form
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

from pydantic import Field,field_validator,ValidationError
from main_stuff.database import engine
from main_stuff.models import login_rule,sign_up_rule
from main_stuff.database import SessionLocal
import main_stuff.database_models


app=FastAPI()

main_stuff.database_models.Base.metadata.create_all(bind=engine)

#later use env
min_pass_len=6
max_pass_len=10

#db=SessionLocal()



def validate_password(password:str):
    if len(password)<min_pass_len or len(password)>max_pass_len:
        raise ValueError("Invalid password Length Can't accept it !!! ")
    pass

    return password

templates= Jinja2Templates(directory="templates")

@app.get("/login")
async def load_login_page(request:Request)->Response:
    return templates.TemplateResponse("login.html",{"request":request})

@app.get("/signup")
async def load_signup_page(request:Request)->Response:
    return templates.TemplateResponse("signup.html",{"request":request})


def validate_login(username,password):
    try:
        return login_rule(username=username,password=password)
    except ValidationError as e:
        print(e.errors()) 
    
@app.post("/login")
async def login_user(response:Response,username:str =Form(...),password:str=Form(...)):
    
    valid_username_rules=validate_login(username,password)
    
    
    print(valid_username_rules)
    if username == "snap00989800" and password == "1234567890" and valid_username_rules:
        return JSONResponse(content={"Login":True},status_code=200)
    return JSONResponse(content={"Login":False},status_code=401)

def validate_signup(username,password,confirm_password,email):
    try:
        return sign_up_rule(username=username,
                            password=password,
                            email=email,
                            confirm_password=confirm_password) and (password==confirm_password)
    except ValidationError as e:
        print(e.errors()) 

@app.post("/signup")
async def signup_user(response:Response,
                      username:str =Form(...),
                      password:str=Form(...),
                      confirm_password:str=Form(...),
                      email:str=Form(...)):
    
    valid_signup_attempt=validate_signup(username=username,
                                         password=password,
                                         confirm_password=confirm_password,
                                         email=email)
    print(valid_signup_attempt)
    db.query()
    if valid_signup_attempt:
        return JSONResponse(content={"Signup":True},status_code=200)
    return JSONResponse(content={"Signup":False},status_code=401)
    