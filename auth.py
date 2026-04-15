import os
import streamlit as st

LOGO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Logo Meta.png")


def require_login() -> None:
    """
    Blocca la pagina corrente finché l'utente non effettua il login.
    Le credenziali sono lette da st.secrets["credentials"].
    """
    if st.session_state.get("logged_in"):
        return

    # Centrato e con logo
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if os.path.exists(LOGO_PATH):
            st.image(LOGO_PATH, width=200)
        st.markdown("## Accesso riservato")
        st.markdown("Inserisci le credenziali per accedere ai questionari.")

        with st.form("login_form", clear_on_submit=False):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Accedi", use_container_width=True)

        if submitted:
            creds = st.secrets.get("credentials", {})
            if username == creds.get("username") and password == creds.get("password"):
                st.session_state["logged_in"] = True
                st.rerun()
            else:
                st.error("Credenziali non valide. Riprova.")

    st.stop()
