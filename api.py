from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import io
from PIL import Image
import cv2
from Calc_Engine import rotate_solid
from Jarvis import jarvis_pipeline

app = FastAPI(title="Smart-Sizer API") #creates HTTP

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/") #decorator, when someone visits this 
#this next line is executed
def root():
    return {"Checker": "API works"} #makes sure the app works

@app.post("/scan")
async def scan_object(file: UploadFile = File(...), pixel_cm: float = 10):
    if file.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
        raise HTTPException(status_code = 400, detail= "File must be an image. Got:" + file.content_type)
    try:
        contents = await file.read()

        pil_img = Image.open(io.BytesIO(contents)).convert("RGB")
        img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

    except Exception as e:
        raise HTTPException(status_code=500, detail =str(e))
    