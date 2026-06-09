from fastapi import FastAPI, File, UploadFile, HTTPException

app = FastAPI() #creates HTTP

app.get("/") #decorator, when someone visits this 
#this next line is executed
def root():
    return {"Hello": "World"}