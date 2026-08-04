import time

import streamlit as st

from api.client import (
    process_document,
    get_progress,
    get_result
)


def render_generator():

    if st.session_state.job_id is None:
        return

    st.subheader("⚙️ Generate Teacher Package")

    if st.button(
        "Generate Teacher Package",
        use_container_width=True,
        disabled=st.session_state.processing
    ):

        st.session_state.processing = True

        process_document(
            st.session_state.job_id
        )

        progress_bar = st.progress(0)

        stage_text = st.empty()

        while True:

            progress = get_progress(
                st.session_state.job_id
            )

            if progress["progress"] == -1:
                st.error(
                    f"Job failed: {progress['stage']}"
                )
                st.session_state.processing = False
                return

            progress_bar.progress(
                progress["progress"]
            )

            stage_text.info(
                progress["stage"]
            )

            if progress["progress"] == 100:
                break

            time.sleep(2)

        result = get_result(
            st.session_state.job_id
        )

        st.session_state.teacher_package = result["teacher_package"]

        st.session_state.files = result["files"]

        st.session_state.published_documents = result["published_documents"]

        st.session_state.completed = True

        st.session_state.processing = False

        st.success(
            "Teacher Knowledge Package generated successfully!"
        )