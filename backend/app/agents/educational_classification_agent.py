import json

from app.schemas.document import DocumentSchema
from app.schemas.classification import ClassificationSchema

from app.utils.llm_client import LLMClient
from app.utils.prompt_loader import load_prompt


class EducationalClassificationAgent:

    def __init__(self):
        self.llm = LLMClient()

    def run(
        self,
        document: DocumentSchema
    ) -> ClassificationSchema:

        prompt = load_prompt(
            "educational_classification"
        )

        response = self.llm.generate(
            prompt=prompt,
            content=document.markdown
        )

        data = json.loads(response)

        return ClassificationSchema(**data)