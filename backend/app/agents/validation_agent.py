from app.schemas.teacher_package import TeacherKnowledgePackage
from app.schemas.validation import ValidationSchema


class ValidationAgent:

    def run(
        self,
        teacher_package: TeacherKnowledgePackage
    ) -> ValidationSchema:

        warnings = []

        if not teacher_package.knowledge.learning_objectives:
            warnings.append("Missing learning objectives.")

        if not teacher_package.knowledge.key_concepts:
            warnings.append("Missing key concepts.")

        if not teacher_package.teaching_plan.lesson_sections:
            warnings.append("Teaching plan has no lesson sections.")

        if not teacher_package.classroom_content.teacher_script:
            warnings.append("Teacher script is empty.")

        if not teacher_package.evaluation.mcqs:
            warnings.append("No MCQs generated.")

        return ValidationSchema(
            is_valid=len(warnings) == 0,
            warnings=warnings
        )