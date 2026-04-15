import streamlit as st
import os
from auth import require_login

st.set_page_config(page_title="Questionari Meta", layout="centered")

require_login()

LOGO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Logo Meta.png")

# Logo in cima
if os.path.exists(LOGO_PATH):
    st.image(LOGO_PATH, width=200)

st.title("Portale Questionari")
st.markdown("Seleziona il questionario che desideri compilare.")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style="
            border: 2px solid #1976D2;
            border-radius: 12px;
            padding: 28px 20px;
            text-align: center;
            background-color: #E3F2FD;
        ">
            <h3 style="color:#1976D2; margin-bottom:10px;">📋 Questionario 1</h3>
            <p style="color:#333; font-size:15px;">Valutazione del livello di rischio per i servizi TIC bancari.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("")
    st.page_link(
        "pages/1_Questionario_Rischio_ICT.py",
        label="Apri Questionario 1",
        use_container_width=True,
    )

with col2:
    st.markdown(
        """
        <div style="
            border: 2px solid #388E3C;
            border-radius: 12px;
            padding: 28px 20px;
            text-align: center;
            background-color: #E8F5E9;
        ">
            <h3 style="color:#388E3C; margin-bottom:10px;">📋 Questionario 2</h3>
            <p style="color:#333; font-size:15px;">Valutazione delle misure di sicurezza ICT del fornitore.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("")
    st.page_link(
        "pages/2_Questionario_Sicurezza_ICT_Fornitori.py",
        label="Apri Questionario 2",
        use_container_width=True,
    )

# Logout nella sidebar
with st.sidebar:
    st.markdown("---")
    if st.button("Esci", use_container_width=True):
        st.session_state["logged_in"] = False
        st.rerun()
