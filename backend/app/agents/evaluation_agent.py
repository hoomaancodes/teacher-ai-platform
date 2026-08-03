import json

from app.schemas.classification import ClassificationSchema
from app.schemas.knowledge import KnowledgeSchema
from app.schemas.teaching_plan import TeachingPlanSchema
from app.schemas.classroom_content import ClassroomContentSchema
from app.schemas.evaluation import EvaluationSchema

from app.utils.llm_client import LLMClient
from app.utils.prompt_loader import load_prompt


class EvaluationAgent:

    def __init__(self):
        self.llm = LLMClient()

    def run(
        self,
        classification: ClassificationSchema,
        knowledge: KnowledgeSchema,
        teaching_plan: TeachingPlanSchema,
        classroom_content: ClassroomContentSchema
    ) -> EvaluationSchema:

        prompt = load_prompt("evaluation")

        content = f"""
Classification

{classification.model_dump_json(indent=2)}

Knowledge

{knowledge.model_dump_json(indent=2)}

Teaching Plan

{teaching_plan.model_dump_json(indent=2)}

Classroom Content

{classroom_content.model_dump_json(indent=2)}
"""

        response = self.llm.generate(
            prompt=prompt,
            content=content
        )

        data = json.loads(response)

        return EvaluationSchema(**data)