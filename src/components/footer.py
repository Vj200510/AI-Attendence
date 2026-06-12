import streamlit as st


def footer_home():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
            <p style="font-weight:bold; color:white;"> Created with ❤️ by Vishal Jain</p>  
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
            <p style="font-weight:bold; color:#1F2235;"> Created with ❤️ by Vishal Jain</p>  
        </div>
    """, unsafe_allow_html=True)
