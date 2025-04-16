from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import student_routes
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include student routes
app.include_router(student_routes.router)
@app.get("/test")
def test():
    return {"message": "Server is working!"}
