from pydantic import BaseModel
from typing import List, Optional


class Page(BaseModel):
    page_number: int
    text: str


class DocumentMetadata(BaseModel):
    job_id: str
    filename: str
    page_count: int
    title: Optional[str] = None
    author: Optional[str] = None
    parser: str


class DocumentSchema(BaseModel):
    metadata: DocumentMetadata
    raw_text: str
    markdown: str
    pages: List[Page]