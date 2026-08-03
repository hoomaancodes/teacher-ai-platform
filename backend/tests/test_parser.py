from pathlib import Path
import uuid

from app.parsers.pdf_parser import PDFParser

parser = PDFParser()

document = parser.parse(
    pdf_path=Path("app/storage/uploads/jess101.pdf"),
    job_id=str(uuid.uuid4())
)

print(document.metadata)
print(document.metadata.page_count)
print(document.markdown[:200])