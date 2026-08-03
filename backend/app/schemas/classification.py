from pydantic import BaseModel


class ClassificationSchema(BaseModel):
    subject: str
    grade: str
    topic: str
    difficulty: str
    language: str