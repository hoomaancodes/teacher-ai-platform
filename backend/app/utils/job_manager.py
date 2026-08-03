from typing import Dict


class JobManager:

    def __init__(self):
        self.jobs: Dict[str, dict] = {}

    def create_job(self, job_id: str):
        self.jobs[job_id] = {
            "progress": 0,
            "stage": "Uploaded"
        }

    def update_progress(
        self,
        job_id: str,
        progress: int,
        stage: str
    ):
        if job_id in self.jobs:
            self.jobs[job_id]["progress"] = progress
            self.jobs[job_id]["stage"] = stage

    def complete_job(self, job_id: str):
        if job_id in self.jobs:
            self.jobs[job_id]["progress"] = 100
            self.jobs[job_id]["stage"] = "Completed"

    def fail_job(self, job_id: str, message: str):
        if job_id in self.jobs:
            self.jobs[job_id]["progress"] = -1
            self.jobs[job_id]["stage"] = f"Failed: {message}"

    def get_progress(self, job_id: str):

        return self.jobs.get(
            job_id,
            {
                "progress": 0,
                "stage": "Job not found"
            }
        )


job_manager = JobManager()