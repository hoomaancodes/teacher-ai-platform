from pathlib import Path

from app.pipeline.orchestrator import PipelineOrchestrator
from app.agents.publisher_agent import PublisherAgent

orchestrator = PipelineOrchestrator()

teacher_package = orchestrator.run(
    pdf_path=Path("app/storage/uploads/b3cf9022-e2b1-4bff-93d8-f0b7e9dc4800.pdf"),
    job_id="test_job"
)

agent = PublisherAgent()

published_content = agent.run(
    teacher_package
)

print("=" * 80)
print("LESSON PLAN")
print("=" * 80)
print(published_content.lesson_plan)

print("\n" + "=" * 80)
print("TEACHER GUIDE")
print("=" * 80)
print(published_content.teacher_guide)

print("\n" + "=" * 80)
print("ASSESSMENT")
print("=" * 80)
print(published_content.assessment)