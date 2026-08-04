from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter()

OUTPUT_DIR = Path("app/storage/outputs")


@router.get("/download/{job_id}/{file_type}")
def download_file(job_id: str, file_type: str):

    files = {
        "json": f"{job_id}_TeacherKnowledgePackage.json",
        "lesson_plan": f"{job_id}_LessonPlan.md",
        "teacher_guide": f"{job_id}_TeacherGuide.md",
        "assessment": f"{job_id}_Assessment.md"
    }

    if file_type not in files:
        raise HTTPException(
            status_code=404,
            detail="Invalid file type."
        )

    file_path = OUTPUT_DIR / files[file_type]

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="File not found."
        )

    return FileResponse(
        path=file_path,
        filename=file_path.name,
        media_type="application/octet-stream"
    )