import json
from pathlib import Path

from fastapi import APIRouter, HTTPException


router = APIRouter()

OUTPUT_DIR = Path("app/storage/outputs")


@router.get("/result/{job_id}")
async def get_result(job_id: str):

    json_path = OUTPUT_DIR / f"{job_id}_TeacherKnowledgePackage.json"

    if not json_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Teacher Knowledge Package not found."
        )

    with open(
        json_path,
        "r",
        encoding="utf-8"
    ) as f:
        teacher_package = json.load(f)

    lesson_path = OUTPUT_DIR / f"{job_id}_LessonPlan.md"
    teacher_path = OUTPUT_DIR / f"{job_id}_TeacherGuide.md" 
    assessment_path = OUTPUT_DIR / f"{job_id}_Assessment.md"

    lesson_plan = (OUTPUT_DIR / f"{job_id}_LessonPlan.md").read_text(encoding="utf-8") if lesson_path.exists() else ""
    teacher_guide = (OUTPUT_DIR / f"{job_id}_TeacherGuide.md").read_text(encoding="utf-8") if teacher_path.exists() else ""
    assessment = (OUTPUT_DIR / f"{job_id}_Assessment.md").read_text(encoding="utf-8") if assessment_path.exists() else ""

    return {
        "job_id": job_id,
        "teacher_package": teacher_package,
        "published_documents": {
            "lesson_plan": lesson_plan,
            "teacher_guide": teacher_guide,
            "assessment": assessment
        },
        "files": {
            "json": f"{job_id}_TeacherKnowledgePackage.json",
            "lesson_plan": f"{job_id}_LessonPlan.md",
            "teacher_guide": f"{job_id}_TeacherGuide.md",
            "assessment": f"{job_id}_Assessment.md"
        }
    }