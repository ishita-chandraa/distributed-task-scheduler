from uuid import uuid4
from uuid import UUID

from app.models.job import Job, JobCreate, JobStatus
from app.storage.memory import jobs

def create_job(job_create: JobCreate):
    job_id= uuid4()
    job=Job(
        id=job_id,
        status=JobStatus.PENDING,
        task=job_create.task,
        payload=job_create.payload)
    jobs[job.id]=job
    return job

def get_job(job_id: UUID):
    return jobs.get(job_id)