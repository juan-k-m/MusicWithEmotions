from datetime import datetime
import pytz

import pandas as pd

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# http://127.0.0.1:8000/predict?pickup_datetime=2012-10-06 12:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2

@app.get("/")
def index():
    return dict(greeting="hello")

#retrieve image from the user

#call the module Face recognition -> make the prediction -> happy

#encoder module is going to tranform concept into musical notes -> one bar (5-6 notes)

#music generation is going to load the model and pass the notes

#model creates the samll piece of music and returns a midi file




