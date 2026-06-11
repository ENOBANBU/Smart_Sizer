from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import io
from PIL import Image
import cv2
from Calc_Engine import rotate_solid
from Jarvis import jarvis_pipeline

app = FastAPI() #creates HTTP

app.get("/") #decorator, when someone visits this 
#this next line is executed
def root():
    return {"Hello": "World"}