from fastapi import APIRouter, HTTPException

from app.utils.job_manager import job_manager


router = APIRouter()


@router.get("/progress/{job_id}")
async def get_progress(job_id: str):

    progress = job_manager.get_progress(job_id)

    if progress["stage"] == "Job not found":
        raise HTTPException(
            status_code=404,
            detail="Job not found."
        )

    return progress