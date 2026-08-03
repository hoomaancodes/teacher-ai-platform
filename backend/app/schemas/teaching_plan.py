from pydantic import BaseModel
from typing import List


class LessonSection(BaseModel):
    title: str
    duration_minutes: int
    objectives: List[str]


class TeachingPlanSchema(BaseModel):
    total_duration: int
    lesson_sections: List[LessonSection]