from pathlib import Path

from app.pipeline.orchestrator import PipelineOrchestrator

orchestrator = PipelineOrchestrator()

teacher_package = orchestrator.run(
    pdf_path=Path("app/storage/uploads/b3cf9022-e2b1-4bff-93d8-f0b7e9dc4800.pdf"),
    job_id="test_job"
)

print(teacher_package.model_dump_json(indent=4))