import json

from app.schemas.classification import ClassificationSchema
from app.schemas.knowledge import KnowledgeSchema
from app.schemas.teaching_plan import TeachingPlanSchema
from app.schemas.classroom_content import ClassroomContentSchema

from app.utils.llm_client import LLMClient
from app.utils.prompt_loader import load_prompt


class ClassroomContentAgent:

    def __init__(self):
        self.llm = LLMClient()

    def run(
        self,
        classification: ClassificationSchema,
        knowledge: KnowledgeSchema,
        teaching_plan: TeachingPlanSchema
    ) -> ClassroomContentSchema:

        prompt = load_prompt("classroom_content")

        content = f"""
Classification

{classification.model_dump_json(indent=2)}

Knowledge

{knowledge.model_dump_json(indent=2)}

Teaching Plan

{teaching_plan.model_dump_json(indent=2)}
"""

        response = self.llm.generate(
            prompt=prompt,
            content=content
        )

        data = json.loads(response)

        return ClassroomContentSchema(**data)