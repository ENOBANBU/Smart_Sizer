from fastapi import FastAPI, File, UploadFile, HTTPException

import cv2
from Calc_Engine import rotate_solid
from Jarvis import jarvis_pipeline

app = FastAPI() #creates HTTP

app.get("/") #decorator, when someone visits this 
#this next line is executed
def root():
    return {"Hello": "World"}