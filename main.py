from fastapi import FastAPI
from datetime import datetime

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from sqlalchemy.exc import OperationalError

import os



def check_env_variables():
    required_env_vars = ["M_DB_USER", "M_DB_PASS", "M_DB_PORT", "M_DB_NAME"]
    missing_vars = [var for var in required_env_vars if not os.environ.get(var)]
    
    if missing_vars:
        return False
    
    return True

check_env_variables()

DATABASE_URL = "postgresql://{}:{}@localhost:{}/{}".format(os.environ.get('M_DB_USER'),
                                                           os.environ.get('M_DB_PASS'),
                                                           os.environ.get('M_DB_PORT'),
                                                           os.environ.get('M_DB_NAME'))
engine = None
if check_env_variables():
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    metadata = MetaData()
    

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello. Today is {}th day of the week!".format(datetime.today().weekday())}

@app.get("/books")
def books():
    if not engine:
        return {"status": "DB connection failed"}

    try:
        with engine.connect() as conn:
            res = conn.execute(text("SELECT * FROM books")).mappings()
            books = [dict(row) for row in res]
    except OperationalError:
        return {"status": "DB connection failed"}
    return {"books": books}