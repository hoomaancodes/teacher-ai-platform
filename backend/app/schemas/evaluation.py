from pydantic import BaseModel
from typing import List


class Activity(BaseModel):
    title: str
    duration_minutes: int
    materials: List[str]
    teacher_instructions: str
    success_criteria: str


class MCQ(BaseModel):
    question: str
    options: List[str]
    answer: str


class ShortAnswer(BaseModel):
    question: str
    answer: str


class LearningGap(BaseModel):
    misconception: str
    diagnostic_question: str
    remediation: str


class EvaluationSchema(BaseModel):
    activities: List[Activity]

    mcqs: List[MCQ]

    short_answer_questions: List[ShortAnswer]

    learning_gaps: List[LearningGap]