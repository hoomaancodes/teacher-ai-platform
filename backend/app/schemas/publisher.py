from pydantic import BaseModel


class PublisherSchema(BaseModel):

    lesson_plan: str

    teacher_guide: str

    assessment: str