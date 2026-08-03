from pydantic import BaseModel
from typing import List


class ClassroomContentSchema(BaseModel):
    entry_ticket: List[str]

    teacher_script: List[str]

    blackboard_notes: List[str]

    classroom_activities: List[str]

    checkpoint_questions: List[str]

    exit_ticket: List[str]

    homework: List[str]

    mentor_moment: str