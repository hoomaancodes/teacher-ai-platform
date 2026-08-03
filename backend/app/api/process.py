import threading
from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.pipeline.orchestrator import PipelineOrchestrator
from app.utils.job_manager import job_manager

router = APIRouter()

UPLOAD_DIR = Path("app/storage/uploads")
OUTPUT_DIR = Path("app/storage/outputs")

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

orchestrator = PipelineOrchestrator()


def run_pipeline(
    pdf_path: Path,
    job_id: str
):

    try:

        teacher_package, published_content = orchestrator.run(
            pdf_path=pdf_path,
            job_id=job_id
        )

        json_path = OUTPUT_DIR / f"{job_id}_TeacherKnowledgePackage.json"

        json_path.write_text(
            teacher_package.model_dump_json(indent=4),
            encoding="utf-8"
        )

        (OUTPUT_DIR / f"{job_id}_LessonPlan.md").write_text(
            published_content.lesson_plan,
            encoding="utf-8"
        )

        (OUTPUT_DIR / f"{job_id}_TeacherGuide.md").write_text(
            published_content.teacher_guide,
            encoding="utf-8"
        )

        (OUTPUT_DIR / f"{job_id}_Assessment.md").write_text(
            published_content.assessment,
            encoding="utf-8"
        )

    except Exception as e:

        job_manager.fail_job(
            job_id,
            str(e)
        )


@router.post("/process/{job_id}")
async def process_document(job_id: str):

    pdf_path = UPLOAD_DIR / f"{job_id}.pdf"

    if not pdf_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Uploaded PDF not found."
        )

    thread = threading.Thread(
        target=run_pipeline,
        args=(
            pdf_path,
            job_id
        ),
        daemon=True
    )

    thread.start()

    return {
        "message": "Processing started.",
        "job_id": job_id
    }