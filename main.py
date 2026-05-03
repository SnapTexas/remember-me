from fastapi import FastAPI
from fastapi.responses import HTMLResponse,JSONResponse
from pydantic import BaseModel,EmailStr,Field,field_validator
from typing import Type,Union
from typing_extensions import Annotated

app=FastAPI()

#later use env
min_pass_len=6
max_pass_len=10



Username=Annotated[str,Field(min_length=4,max_length=20,pattern=r'^(?=.*[0-9])(?=.*[!@#$%^&*]).+$')]
Password=Annotated[str,Field(min_length=6,max_length=10)]



def validate_password(password:str):
    if len(password)<min_pass_len or len(password)>max_pass_len:
        raise ValueError("Invalid password Length Can't accept it !!! ")
    pass

    return password
class login(BaseModel):
    username:Union[EmailStr,Username]    
    password:str

class sign_up(BaseModel):
    email:EmailStr
    username:Username
    password:str
    confirm_password:str


@app.get("/")
async def home():
    return JSONResponse(status_code=200,content={"data":"hello world"})

