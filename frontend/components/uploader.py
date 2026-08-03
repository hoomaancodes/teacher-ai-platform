import streamlit as st

from api.client import upload_pdf


def render_uploader():

    st.subheader("📄 Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if uploaded_file is None:
        return

    if st.button(
        "Upload PDF",
        use_container_width=True
    ):

        try:

            data = upload_pdf(uploaded_file)

            st.session_state.job_id = data["job_id"]

            st.success("PDF uploaded successfully!")

            st.info(
                "Click **Generate Teacher Package** to start processing."
            )

        except Exception as e:

            st.error(str(e))