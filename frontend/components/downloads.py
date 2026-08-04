from pathlib import Path

import streamlit as st


OUTPUT_DIR = Path("../backend/app/storage/outputs")


def render_downloads():

    if not st.session_state.completed:
        return

    st.header("⬇️ Download Generated Resources")

    files = st.session_state.files

    col1, col2, col3, col4 = st.columns(4)

    download_items = [
        (
            col1,
            "📦 Teacher Package",
            files["json"]
        ),
        (
            col2,
            "📘 Lesson Plan",
            files["lesson_plan"]
        ),
        (
            col3,
            "👨‍🏫 Teacher Guide",
            files["teacher_guide"]
        ),
        (
            col4,
            "📝 Assessment",
            files["assessment"]
        )
    ]

    for column, label, filename in download_items:

        file_path = OUTPUT_DIR / filename

        if file_path.exists():

            with column:

                with open(file_path, "rb") as f:

                    st.download_button(
                        label=label,
                        data=f,
                        file_name=filename,
                        use_container_width=True
                    )

'''
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
'''