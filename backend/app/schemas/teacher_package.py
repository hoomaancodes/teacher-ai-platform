from typing import Optional
from pydantic import BaseModel

from app.schemas.document import DocumentSchema
from app.schemas.classification import ClassificationSchema
from app.schemas.knowledge import KnowledgeSchema
from app.schemas.teaching_plan import TeachingPlanSchema
from app.schemas.classroom_content import ClassroomContentSchema
from app.schemas.evaluation import EvaluationSchema
from app.schemas.validation import ValidationSchema

class TeacherKnowledgePackage(BaseModel):
    document: DocumentSchema
    classification: ClassificationSchema
    knowledge: KnowledgeSchema
    teaching_plan: TeachingPlanSchema
    classroom_content: ClassroomContentSchema
    evaluation: EvaluationSchema
    validation: Optional[ValidationSchema] = None