import json
from pathlib import Path

from app.parsers.pdf_parser import PDFParser
from app.schemas.document import DocumentSchema


class DocumentIntelligenceAgent:

    def __init__(self):
        self.parser = PDFParser()

    def run(
        self,
        pdf_path: Path,
        job_id: str
    ) -> DocumentSchema:

        document = self.parser.parse(
            pdf_path=pdf_path,
            job_id=job_id
        )

        output_path = Path("app/storage/parsed")
        output_path.mkdir(parents=True, exist_ok=True)

        with open(
            output_path / f"{job_id}.json",
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                document.model_dump(),
                file,
                indent=4,
                ensure_ascii=False
            )

        return document