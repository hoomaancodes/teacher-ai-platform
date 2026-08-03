import json

from app.schemas.teacher_package import TeacherKnowledgePackage
from app.schemas.publisher import PublisherSchema

from app.utils.llm_client import LLMClient
from app.utils.prompt_loader import load_prompt


class PublisherAgent:

    def __init__(self):
        self.llm = LLMClient()

    def run(
        self,
        teacher_package: TeacherKnowledgePackage
    ) -> PublisherSchema:

        prompt = load_prompt(
            "publisher"
        )

        export_input = {
            "classification": teacher_package.classification.model_dump(),
            "knowledge": teacher_package.knowledge.model_dump(),
            "teaching_plan": teacher_package.teaching_plan.model_dump(),
            "classroom_content": teacher_package.classroom_content.model_dump(),
            "evaluation": teacher_package.evaluation.model_dump(),
            "validation": teacher_package.validation.model_dump()
        }

        response = self.llm.generate(
            prompt=prompt,
            content=json.dumps(
                export_input,
                indent=2
            )
        )

        data = json.loads(response)

        return PublisherSchema(**data)