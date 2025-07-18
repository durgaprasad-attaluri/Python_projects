from fastapi import FastAPI

# Simple API

## Creating an app object
app=FastAPI()  # - it is like switch on

## Define endpoint
@app.get("/") # Home page(@ attaches the functions below it)

## Function
def hello():
    return {'message' : 'Hello World!'}

@app.get("/about")
def about():
    return {'About' : 'This is about FastAPI'}