import streamlit as st
from api.client import download_file


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
            "json"
        ),
        (
            col2,
            "📘 Lesson Plan",
            "lesson_plan"
        ),
        (
            col3,
            "👨‍🏫 Teacher Guide",
            "teacher_guide"
        ),
        (
            col4,
            "📝 Assessment",
            "assessment"
        )
    ]

    for column, label, file_type in download_items:

        with column:

            data = download_file(
                st.session_state.job_id,
                file_type
            )

            st.download_button(
                label=label,
                data=data,
                file_name=files[file_type],
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