import streamlit as st

from styles import load_css #styles

from components.uploader import render_uploader
from components.generator import render_generator
from components.preview import render_preview
from components.downloads import render_downloads

st.set_page_config(
    page_title="Teacher AI Platform",
    page_icon="📚",
    layout="wide"
)

load_css() #styles

#st.title("📚 Teacher AI Platform")
#styles
st.markdown(
    """
<div class="hero-title">
📚 Teacher AI Platform
</div>
""",
    unsafe_allow_html=True,
)

st.write("")   # small vertical gap

#styles
st.markdown(
    """
<div class="hero-subtitle">

Transform educational PDFs into structured lesson plans,
classroom resources, assessments, and teacher-ready knowledge packages.

</div>
""",
    unsafe_allow_html=True,
)

#st.caption(
#    "Transform educational PDFs into teacher-ready knowledge packages."
#)

#styles
st.markdown(
    """
<marquee behavior="scroll" direction="left" scrollamount="5"
style="
font-size:20px;
font-weight:600;
color:#0F766E;
padding:10px 0;
">
📜&nbsp;
अन्नदानं परं दानं विद्यादानमतः परम् ।
अन्नेन क्षणिका तृप्तिर्यावज्जीवं च विद्यया ॥
</marquee>
""",
    unsafe_allow_html=True,
)

st.write("")   # small vertical gap

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

st.divider() #divider

render_generator()

render_preview()

render_downloads()


st.divider()

left, center, right = st.columns([3, 3, 1])

with left:
    st.markdown("**Teacher AI Platform © 2026**")

with center:
    st.markdown("Developed by **Maan Kaur**")

with right:
    st.markdown(
        """
<a href="https://github.com/hoomaancodes" target="_blank" style="text-decoration:none;">
GitHub
</a>
&nbsp;&nbsp;•&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/maankaur23/" target="_blank" style="text-decoration:none;">
LinkedIn
</a>
""",
        unsafe_allow_html=True,
    )