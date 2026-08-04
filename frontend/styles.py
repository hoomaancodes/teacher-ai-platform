import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/* Google Font */

@import url('https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;600;700;800&display=swap');


/* Apply font only to app */

.stApp{
    font-family:'Work Sans',sans-serif;
}


/* Layout */

.block-container{
    max-width:90%;
    padding-top:3rem;
}


/* Hero Title */

.hero-title{
    font-size:48px;
    font-weight:800;
    color:#2B2D42;
    margin-bottom:8px;
}


/* Hero Subtitle */

.hero-subtitle{
    font-size:20px;
    color:#64748B;
    line-height:1.6;
    margin-bottom:20px;
}


/* Footer */

.footer{
    text-align:center;
    color:#555;
    line-height:1.8;
    margin-top:30px;
    margin-bottom:10px;
}

.footer a{
    text-decoration:none;
}

</style>
""",
        unsafe_allow_html=True,
    )