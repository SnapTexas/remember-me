from pydantic import BaseModel,EmailStr,Field
from typing import Type,Union 

from typing_extensions import Annotated

Username=Annotated[str,Field(min_length=4,max_length=20)]
Password=Annotated[str,Field(min_length=6,max_length=10)]

class login_rule(BaseModel):
    username:Union[EmailStr,Username]    
    password:str

class sign_up_rule(BaseModel):
    email:EmailStr
    username:Username
    password:Password
    confirm_password:Password

