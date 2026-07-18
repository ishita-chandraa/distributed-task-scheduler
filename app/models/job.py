from uuid import UUID
from enum import Enum
from typing import Any

from pydantic import BaseModel


class JobStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    

class JobCreate(BaseModel):
    task: str
    payload: dict[str, Any]


class Job(BaseModel):
    id: UUID
    status: JobStatus
    task: str
    payload: dict[str, Any]
