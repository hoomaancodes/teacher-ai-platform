from pathlib import Path
import fitz
import pymupdf4llm

from app.schemas.document import (
    DocumentSchema,
    DocumentMetadata,
    Page
)


class PDFParser:

    def parse(
        self,
        pdf_path: Path,
        job_id: str
    ) -> DocumentSchema:

        doc = fitz.open(pdf_path)

        metadata = DocumentMetadata(
            job_id=job_id,
            filename=pdf_path.name,
            page_count=len(doc),
            title=doc.metadata.get("title") or None,
            author=doc.metadata.get("author") or None,
            parser="PyMuPDF4LLM"
        )

        markdown = pymupdf4llm.to_markdown(str(pdf_path))

        pages = []

        for page_number, page in enumerate(doc, start=1):

            pages.append(
                Page(
                    page_number=page_number,
                    text=page.get_text()
                )
            )
        raw_text = "\n\n".join(
            page.text for page in pages
            )
        

        result = DocumentSchema(
            metadata=metadata,
            raw_text=raw_text,
            markdown=markdown,
            pages=pages
        )

        doc.close()

        return result