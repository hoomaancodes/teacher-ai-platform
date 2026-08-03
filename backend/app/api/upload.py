from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import shutil
from uuid import uuid4
from app.utils.job_manager import job_manager

router = APIRouter()

UPLOAD_DIR = Path("app/storage/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    # Validate PDF
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    job_id = str(uuid4())
    job_manager.create_job(job_id)

    # Save the uploaded file to the storage directory
    file_path = UPLOAD_DIR / f"{job_id}.pdf"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer) #Copies the uploaded file's contents from FastAPI's file object into the file on disk.

    # Return a success response with the file path
    return {
        "message": "Document uploaded and parsed successfully.",
        "job_id": job_id,
        "filename": file.filename
    }