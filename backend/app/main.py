from fastapi import FastAPI
from app.api.upload import router as upload_router
from app.api.process import router as process_router
from app.api.progress import router as progress_router
from app.api.result import router as result_router

app = FastAPI(
    title="Teacher AI Platform",
    version="1.0.0"
)

app.include_router(upload_router)
app.include_router(process_router)
app.include_router(progress_router)
app.include_router(result_router)

@app.get("/")
def root():
    return {
        "message": "Teacher AI Platform API is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }