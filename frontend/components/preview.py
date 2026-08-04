from pathlib import Path

import streamlit as st


def render_preview():

    if not st.session_state.completed:
        return

    package = st.session_state.teacher_package

    st.header("📦 Teacher Knowledge Package")

    package_tabs = st.tabs(
        [
            "Classification",
            "Knowledge",
            "Teaching Plan",
            "Classroom Content",
            "Evaluation",
            "Validation"
        ]
    )

    with package_tabs[0]:
        st.json(package["classification"])

    with package_tabs[1]:
        st.json(package["knowledge"])

    with package_tabs[2]:
        st.json(package["teaching_plan"])

    with package_tabs[3]:
        st.json(package["classroom_content"])

    with package_tabs[4]:
        st.json(package["evaluation"])

    with package_tabs[5]:
        st.json(package["validation"])

    st.divider()

    st.header("📄 Published Documents")

    files = st.session_state.files
    published = st.session_state.published_documents

    document_tabs = st.tabs(
        [
            "Lesson Plan",
            "Teacher Guide",
            "Assessment"
        ]
    )


    with document_tabs[0]:
        st.markdown(
            published["lesson_plan"]
       )

    with document_tabs[1]:
        st.markdown(
            published["teacher_guide"]
        )

    with document_tabs[2]:
        st.markdown(
            published["assessment"]
        )