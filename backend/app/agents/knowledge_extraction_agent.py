import json

from app.schemas.document import DocumentSchema
from app.schemas.knowledge import KnowledgeSchema

from app.utils.llm_client import LLMClient
from app.utils.prompt_loader import load_prompt


class KnowledgeExtractionAgent:

    def __init__(self):
        self.llm = LLMClient()

    def run(
        self,
        document: DocumentSchema
    ) -> KnowledgeSchema:

        prompt = load_prompt(
            "knowledge_extraction"
        )

        response = self.llm.generate(
            prompt=prompt,
            content=document.markdown
        )

        data = json.loads(response)

        return KnowledgeSchema(**data)