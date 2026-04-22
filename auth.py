"""
Modulo di autenticazione — login page enterprise.
"""
import os
import streamlit as st
from style import apply_custom_theme

LOGO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Logo Meta.png")


def render_login() -> None:
    """Pagina di login professionale, centrata, card bianca su sfondo neutro."""

    # Override sfondo: grigio freddo, non gradiente
    st.markdown("""
    <style>
    .stApp { background-color: #EDF0F5 !important; }
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 90vh;
    }
    /* Nasconde topbar e sidebar durante il login */
    header[data-testid="stHeader"] { display: none !important; }
    [data-testid="stSidebar"],
    [data-testid="stSidebarCollapsedControl"] { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:48px'></div>", unsafe_allow_html=True)

    # Layout centrato
    _, col, _ = st.columns([1, 1.1, 1])

    with col:
        # Logo
        if os.path.exists(LOGO_PATH):
            logo_c, _ = st.columns([1, 2])
            with logo_c:
                st.image(LOGO_PATH)

        # Card header
        st.markdown("""
        <div style="
            background:#FFFFFF;
            border:1px solid #D9E1EA;
            border-top:4px solid #1F3A5F;
            border-radius:6px;
            padding:36px 36px 28px 36px;
            box-shadow:0 4px 24px rgba(21,37,53,0.07);
            margin-top:18px;
        ">
            <p style="color:#4F6B8A;font-size:10px;font-weight:700;text-transform:uppercase;
                      letter-spacing:1.8px;margin:0 0 10px 0;">
                ICT Risk Management · Accesso Riservato
            </p>
            <h2 style="color:#1B2430;font-size:20px;font-weight:700;margin:0 0 4px 0;
                       letter-spacing:-0.3px;">
                Benvenuto nella piattaforma
            </h2>
            <p style="color:#8E97A3;font-size:13px;margin:0 0 28px 0;line-height:1.5;">
                Inserisci le credenziali per accedere all'ambiente riservato.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Form (separato dalla card header per compatibilità Streamlit)
        with st.form("login_form", clear_on_submit=False):
            username = st.text_input("Username", placeholder="Inserisci username")
            password = st.text_input("Password", type="password", placeholder="••••••••")
            submitted = st.form_submit_button(
                "Accedi alla piattaforma →",
                use_container_width=True,
            )

        if submitted:
            creds = st.secrets.get("credentials", {})
            if username == creds.get("username") and password == creds.get("password"):
                st.session_state["logged_in"] = True
                st.rerun()
            else:
                st.error("Credenziali non valide. Verificare username e password.")

        # Footer
        st.markdown("""
        <p style="color:#B8C4CE;font-size:11px;text-align:center;margin-top:20px;">
            © 2025 Meta Advisory & Tech Services S.r.l. — Uso strettamente riservato
        </p>
        """, unsafe_allow_html=True)


def require_login() -> None:
    """Blocca l'accesso alla pagina se l'utente non è autenticato."""
    apply_custom_theme()
    if st.session_state.get("logged_in"):
        return
    render_login()
    st.stop()
