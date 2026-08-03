from pathlib import Path
import uuid

from app.parsers.pdf_parser import PDFParser

from app.agents.educational_classification_agent import (
    EducationalClassificationAgent
)

from app.agents.knowledge_extraction_agent import (
    KnowledgeExtractionAgent
)

from app.agents.teaching_planner_agent import (
    TeachingPlannerAgent
)


# Parse the document
parser = PDFParser()

document = parser.parse(
    Path("app/storage/uploads/b3cf9022-e2b1-4bff-93d8-f0b7e9dc4800.pdf"),
    str(uuid.uuid4())
)

# Classification
classification_agent = EducationalClassificationAgent()

classification = classification_agent.run(document)

# Knowledge Extraction
knowledge_agent = KnowledgeExtractionAgent()

knowledge = knowledge_agent.run(document)

# Teaching Planner
planner = TeachingPlannerAgent()

plan = planner.run(
    classification,
    knowledge
)

print(plan)