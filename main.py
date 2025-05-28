from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello. Today is {}th day of the week!".format(datetime.today().weekday())}

@app.get("/books")
def resources():
    res = [
        {"name": "book1", "category": "cat1", "date_published": "1990"},
        {"name": "book2", "category": "cat2", "date_published": "2002"}
    ]
    return {"books": res}