import requests

API_URL = "http://127.0.0.1:8000"


def upload_pdf(uploaded_file):

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            "application/pdf"
        )
    }

    response = requests.post(
        f"{API_URL}/upload",
        files=files
    )

    response.raise_for_status()

    return response.json()


def process_document(job_id):

    response = requests.post(
        f"{API_URL}/process/{job_id}"
    )

    response.raise_for_status()

    return response.json()


def get_progress(job_id):

    try:

        response = requests.get(
            f"{API_URL}/progress/{job_id}"
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.ConnectionError:

        return {
            "progress": -1,
            "stage": "Backend server is not running."
        }


def get_result(job_id):

    response = requests.get(
        f"{API_URL}/result/{job_id}"
    )

    response.raise_for_status()

    return response.json()