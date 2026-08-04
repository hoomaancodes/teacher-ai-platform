from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router
from app.api.process import router as process_router
from app.api.progress import router as progress_router
from app.api.result import router as result_router
from app.api.download import router as download_router

app = FastAPI(
    title="Teacher AI Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8501",      # Local Streamlit
        "http://127.0.0.1:8501",
        "https://teacher-ai-platformmm.streamlit.app/"      # Local Streamlit
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(upload_router)
app.include_router(process_router)
app.include_router(progress_router)
app.include_router(result_router)
app.include_router(download_router)

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