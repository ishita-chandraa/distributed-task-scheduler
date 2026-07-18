from app.models.job import JobCreate
from fastapi import FastAPI
from uuid import UUID

from app.services import job_service

app = FastAPI(
    title="Distributed Task Scheduler",
    version="1.0.0"
)


@app.post("/jobs")
def create_job(job_create: JobCreate):
    return job_service.create_job(job_create)


@app.get("/jobs/{job_id}")
def get_job(job_id: UUID):
    return job_service.get_job(job_id)