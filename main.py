from fastapi import FastAPI
from datetime import datetime

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from sqlalchemy.exc import OperationalError

import os


def check_db_env_variables():
    required_env_vars = ["M_DB_USER", "M_DB_PASS", "M_DB_PORT", "M_DB_NAME"]
    missing_vars = [var for var in required_env_vars if not os.environ.get(var)]
    
    if missing_vars:
        return False
    
    return True


mode = "reg"
if os.environ.get('FAP_MODE'):
    mode = os.environ.get('FAP_MODE')

engine = None

if mode == "reg" and check_db_env_variables():
    DATABASE_URL = "postgresql://{}:{}@localhost:{}/{}".format(os.environ.get('M_DB_USER'),
                                                               os.environ.get('M_DB_PASS'),
                                                               os.environ.get('M_DB_PORT'),
                                                               os.environ.get('M_DB_NAME'))

    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    metadata = MetaData()
    

app = FastAPI()


@app.get("/")
def read_root():
    return {
            "message": "Hello. Today is {}th day of the week!".format(datetime.today().weekday()),
            "mode": mode
           }

@app.get("/books")
def books():
    if mode == "mock":
        return {"books": 
                [
                    {"id": 1, "title": "1984", "author": "George Orwell"},
                    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
                    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
                ]
                }

    if not engine:
        return {"status": "DB connection failed"}

    try:
        with engine.connect() as conn:
            res = conn.execute(text("SELECT * FROM books")).mappings()
            books = [dict(row) for row in res]
    except OperationalError:
        return {"status": "DB connection failed"}
    return {"books": books}

@app.get("/cpu")
def cpu():

    list_of_squares = [x**2 for x in range(100000)]
    list_of_squares.sort(reverse=True)

    return {"message": "Emulating CPU usage by creating a long random list and sorting it"}