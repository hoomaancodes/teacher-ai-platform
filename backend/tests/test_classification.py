from pathlib import Path
import uuid

from app.parsers.pdf_parser import PDFParser
from app.agents.educational_classification_agent import (
    EducationalClassificationAgent
)

parser = PDFParser()

document = parser.parse(
    Path("app/storage/uploads/b3cf9022-e2b1-4bff-93d8-f0b7e9dc4800.pdf"),
    str(uuid.uuid4())
)

agent = EducationalClassificationAgent()

classification = agent.run(document)

print(classification)