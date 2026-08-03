from pathlib import Path
import uuid

from app.agents.document_intelligence_agent import DocumentIntelligenceAgent

agent = DocumentIntelligenceAgent()

document = agent.run(
    pdf_path=Path("app/storage/uploads/jess101.pdf"),
    job_id=str(uuid.uuid4())
)

print(document.metadata)