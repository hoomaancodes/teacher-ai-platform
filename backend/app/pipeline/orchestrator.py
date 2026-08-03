from pathlib import Path

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

from app.agents.classroom_content_agent import (
    ClassroomContentAgent
)

from app.agents.evaluation_agent import (
    EvaluationAgent
)

from app.agents.validation_agent import (
    ValidationAgent
)

from app.agents.publisher_agent import (
    PublisherAgent
)

from app.schemas.teacher_package import TeacherKnowledgePackage

from app.utils.job_manager import job_manager


class PipelineOrchestrator:

    def __init__(self):

        self.parser = PDFParser()

        self.classification_agent = EducationalClassificationAgent()

        self.knowledge_agent = KnowledgeExtractionAgent()

        self.planner_agent = TeachingPlannerAgent()

        self.classroom_agent = ClassroomContentAgent()

        self.evaluation_agent = EvaluationAgent()

        self.validation_agent = ValidationAgent()

        self.publisher_agent = PublisherAgent()

    def run(
        self,
        pdf_path: Path,
        job_id: str
    ):

        # ---------- Stage 1 : Document Intelligence ----------
        job_manager.update_progress(
            job_id,
            10,
            "Parsing Document"
        )

        document = self.parser.parse(
            pdf_path,
            job_id
        )

        # ---------- Stage 2 : Classification ----------
        job_manager.update_progress(
            job_id,
            25,
            "Educational Classification"
        )

        classification = self.classification_agent.run(
            document
        )

        # ---------- Stage 3 : Knowledge Extraction ----------
        job_manager.update_progress(
            job_id,
            40,
            "Knowledge Extraction"
        )

        knowledge = self.knowledge_agent.run(
            document
        )

        # ---------- Stage 4 : Teaching Planner ----------
        job_manager.update_progress(
            job_id,
            60,
            "Teaching Planning"
        )

        teaching_plan = self.planner_agent.run(
            classification,
            knowledge
        )

        # ---------- Stage 5 : Classroom Content ----------
        job_manager.update_progress(
            job_id,
            80,
            "Generating Classroom Content"
        )

        classroom_content = self.classroom_agent.run(
            classification,
            knowledge,
            teaching_plan
        )

        # ---------- Stage 6 : Evaluation ----------
        job_manager.update_progress(
            job_id,
            90,
            "Generating Assessment"
        )

        evaluation = self.evaluation_agent.run(
            classification,
            knowledge,
            teaching_plan,
            classroom_content
        )

        # ---------- Create Teacher Package ----------
        teacher_package = TeacherKnowledgePackage(
            document=document,
            classification=classification,
            knowledge=knowledge,
            teaching_plan=teaching_plan,
            classroom_content=classroom_content,
            evaluation=evaluation
        )

        # ---------- Stage 7 : Validation ----------
        job_manager.update_progress(
            job_id,
            95,
            "Validation"
        )

        teacher_package.validation = self.validation_agent.run(
            teacher_package
        )

        # ---------- Stage 8 : Publishing ----------
        job_manager.update_progress(
            job_id,
            98,
            "Publishing Documents"
        )

        published_content = self.publisher_agent.run(
            teacher_package
        )

        job_manager.complete_job(job_id)

        return teacher_package, published_content