import os
import streamlit as st
from style import inject_css

LOGO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Logo Meta.png")


def require_login() -> None:
    inject_css()

    if st.session_state.get("logged_in"):
        return

    # Sfondo grigio chiaro per la pagina login
    st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #00338D 0%, #001F6B 100%) !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    col_l, col_c, col_r = st.columns([1, 1.4, 1])
    with col_c:
        # Logo
        if os.path.exists(LOGO_PATH):
            st.image(LOGO_PATH, width=160)
        else:
            st.markdown('<h2 style="color:white;">Meta Advisory</h2>', unsafe_allow_html=True)

        st.markdown("""
        <div style="
            background:white;
            border-radius:4px;
            padding:40px 36px 36px 36px;
            box-shadow:0 8px 32px rgba(0,0,0,0.25);
            border-top:5px solid #00338D;
            margin-top:20px;
        ">
            <p style="color:#00338D;font-size:11px;font-weight:600;letter-spacing:1.5px;
                      text-transform:uppercase;margin-bottom:4px;">Portale ICT Risk</p>
            <h2 style="color:#1A1A2A;font-size:22px;font-weight:700;margin-bottom:4px;">Accedi alla piattaforma</h2>
            <p style="color:#888;font-size:13px;margin-bottom:28px;">Inserisci le credenziali per continuare</p>
        </div>
        """, unsafe_allow_html=True)

        with st.container():
            with st.form("login_form", clear_on_submit=False):
                username = st.text_input("Username", placeholder="Inserisci username")
                password = st.text_input("Password", type="password", placeholder="Inserisci password")
                submitted = st.form_submit_button("Accedi →", use_container_width=True)

            if submitted:
                creds = st.secrets.get("credentials", {})
                if username == creds.get("username") and password == creds.get("password"):
                    st.session_state["logged_in"] = True
                    st.rerun()
                else:
                    st.error("Credenziali non valide. Riprova.")

        st.markdown("""
        <p style="color:rgba(255,255,255,0.4);font-size:11px;text-align:center;margin-top:24px;">
        © 2025 Meta Advisory · Accesso riservato
        </p>
        """, unsafe_allow_html=True)

    st.stop()
