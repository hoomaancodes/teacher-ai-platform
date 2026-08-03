from pydantic import BaseModel
from typing import List


class Concept(BaseModel):
    name: str
    description: str


class KnowledgeSchema(BaseModel):
    learning_objectives: List[str]
    prerequisites: List[str]
    key_concepts: List[Concept]
    keywords: List[str]