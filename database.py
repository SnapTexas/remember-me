from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv,find_dotenv

path=find_dotenv(".env1")
load_dotenv(path)
db_url=str(os.getenv("supabase_direct_connect_url"))
print(db_url)
engine=create_engine(url=db_url)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
