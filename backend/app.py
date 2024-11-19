from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pymongo import MongoClient
from typing import List
from datetime import datetime

from config import MONGODB_URL, MONGODB_USR, MONGODB_PWD, REACT_APP_URL
from schemas import JobApplication

client = MongoClient(MONGODB_URL, username=MONGODB_USR, password=MONGODB_PWD)
app = FastAPI()

# Allow CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[REACT_APP_URL],  # React app URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

db = client["job_tracker"]
collection = db["applications"]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/applications")
async def add_application(application: JobApplication):
    
    application_data = application.model_dump()

    # Convert date_applied (datetime.date) to datetime.datetime
    if application_data["date_applied"]:
        application_data["date_applied"] = datetime.combine(application_data["date_applied"], datetime.min.time())

    result = collection.insert_one(application_data)
    
    return {"message": "Application added successfully", "application_id": str(result.inserted_id)}

@app.get("/applications", response_model=List[JobApplication])
async def get_applications():
    # Fetch all applications from MongoDB
    applications = list(collection.find())
    
    if not applications:
        return {"message": "No applications found."}
    
    return applications

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
