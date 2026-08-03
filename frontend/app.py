import streamlit as st

from components.uploader import render_uploader
from components.generator import render_generator
from components.preview import render_preview
from components.downloads import render_downloads

st.set_page_config(
    page_title="Teacher AI Platform",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Teacher AI Platform")

st.caption(
    "Transform educational PDFs into teacher-ready knowledge packages."
)

if "job_id" not in st.session_state:
    st.session_state.job_id = None

if "teacher_package" not in st.session_state:
    st.session_state.teacher_package = None

if "files" not in st.session_state:
    st.session_state.files = None

if "processing" not in st.session_state:
    st.session_state.processing = False

if "completed" not in st.session_state:
    st.session_state.completed = False

render_uploader()

render_generator()

render_preview()

render_downloads()