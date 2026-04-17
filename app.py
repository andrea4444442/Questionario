import streamlit as st
import os
from auth import require_login
from style import inject_css

st.set_page_config(page_title="ICT Risk Platform", page_icon="🔵", layout="wide")

require_login()
inject_css()

LOGO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Logo Meta.png")

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
col_logo, col_title = st.columns([1, 8])
with col_logo:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, width=90)
with col_title:
    st.markdown("""
    <div style="padding: 8px 0;">
        <p style="color:#00338D;font-size:11px;font-weight:600;letter-spacing:1.5px;
                  text-transform:uppercase;margin:0;">Meta Advisory</p>
        <h1 style="color:#1A1A2A;font-size:26px;font-weight:700;margin:2px 0 0 0;
                   letter-spacing:-0.3px;">ICT Risk Management Platform</h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<hr style="border:none;border-top:2px solid #00338D;margin:12px 0 28px 0;">', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Intro
# ---------------------------------------------------------------------------
st.markdown("""
<p style="color:#555;font-size:15px;max-width:700px;margin-bottom:32px;">
Piattaforma per la valutazione del rischio ICT e delle misure di sicurezza dei fornitori
TIC, in conformità con i requisiti DORA e le best practice di settore.
</p>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Cards
# ---------------------------------------------------------------------------
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div class="nav-card">
        <div class="card-icon">📋</div>
        <h3>Questionario 1</h3>
        <p>Valutazione del livello di rischio inerente per i servizi TIC — disponibilità,
        sicurezza, cambiamenti e integrità dei dati.</p>
        <br>
        <p style="color:#00338D;font-size:12px;font-weight:600;">RISCHIO INERENTE ICT →</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    st.page_link("pages/1_Questionario_Rischio_ICT.py", label="Avvia Questionario 1", use_container_width=True)

with col2:
    st.markdown("""
    <div class="nav-card green">
        <div class="card-icon">🔒</div>
        <h3>Questionario 2</h3>
        <p>Valutazione delle misure di sicurezza ICT del fornitore — certificazioni,
        governance, continuità operativa, IAM e vulnerability management.</p>
        <br>
        <p style="color:#00875A;font-size:12px;font-weight:600;">MISURE DI SICUREZZA →</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    st.page_link("pages/2_Questionario_Sicurezza_ICT_Fornitori.py", label="Avvia Questionario 2", use_container_width=True)

with col3:
    st.markdown("""
    <div class="nav-card purple">
        <div class="card-icon">📊</div>
        <h3>Registro Rischi</h3>
        <p>Riepilogo consolidato del rischio residuo per tutti i servizi TIC valutati,
        con matrice di incrocio e reportistica Excel.</p>
        <br>
        <p style="color:#6554C0;font-size:12px;font-weight:600;">RISCHIO RESIDUO →</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    st.page_link("pages/3_Registro_Rischi.py", label="Apri Registro Rischi", use_container_width=True)

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<hr style="border:none;border-top:1px solid #E0E4EF;margin-bottom:16px;">
<p style="color:#AAB0C0;font-size:12px;text-align:center;">
© 2025 Meta Advisory S.r.l. · Piattaforma ICT Risk Management · Uso riservato
</p>
""", unsafe_allow_html=True)

# Sidebar logout
with st.sidebar:
    st.markdown("""
    <div style="padding:16px 0 8px 0;">
        <p style="font-size:11px;opacity:0.6;text-transform:uppercase;letter-spacing:1px;">Sessione attiva</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    if st.button("Esci dalla piattaforma", use_container_width=True):
        st.session_state["logged_in"] = False
        st.rerun()
