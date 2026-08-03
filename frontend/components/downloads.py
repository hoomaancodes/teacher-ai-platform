from pathlib import Path

import streamlit as st


OUTPUT_DIR = Path("../backend/app/storage/outputs")


def render_downloads():

    if not st.session_state.completed:
        return

    st.header("⬇️ Downloads")

    files = st.session_state.files

    download_items = [
        (
            "Teacher Knowledge Package",
            files["json"]
        ),
        (
            "Lesson Plan",
            files["lesson_plan"]
        ),
        (
            "Teacher Guide",
            files["teacher_guide"]
        ),
        (
            "Assessment",
            files["assessment"]
        )
    ]

    for label, filename in download_items:

        file_path = OUTPUT_DIR / filename

        if file_path.exists():

            with open(
                file_path,
                "rb"
            ) as f:

                st.download_button(
                    label=f"Download {label}",
                    data=f,
                    file_name=filename,
                    use_container_width=True
                )