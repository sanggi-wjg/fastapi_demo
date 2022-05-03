####################################
# Enum 예제
####################################
from enum import Enum

from fastapi import APIRouter

router = APIRouter(
    tags = ["jobs"],
    responses = { 404: { "detail": "not found" } }
)


class JobName(str, Enum):
    Student = "student"
    Teacher = "teacher"
    Programmer = "programmer"


@router.get("/jobs/{job_name}")
async def get_job(job_name: JobName):
    if job_name == JobName.Student:
        return { "job_name": job_name, "message": "Good Student" }
    if job_name == JobName.Programmer:
        return { "job_name": job_name, "message": "Good programmer" }
    return { "job_name": job_name, "message": "Good teacher" }
