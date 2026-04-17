import streamlit as st
import os
from auth import require_login
from style import apply_custom_theme, render_sidebar

st.set_page_config(
    page_title="ICT Risk Platform — Meta Advisory",
    page_icon="▪",
    layout="wide",
    initial_sidebar_state="expanded",
)

require_login()
apply_custom_theme()

LOGO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Logo Meta.png")

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
render_sidebar()

# ---------------------------------------------------------------------------
# Header pagina
# ---------------------------------------------------------------------------
col_logo, col_title = st.columns([1, 9], gap="small")
with col_logo:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, width=110)
with col_title:
    st.markdown("""
    <div style="padding:6px 0 0 4px;">
        <p style="color:#8E97A3;font-size:10px;font-weight:600;text-transform:uppercase;
                  letter-spacing:1.5px;margin:0 0 3px 0;">
            Meta Advisory & Tech Services
        </p>
        <h1 style="color:#1B2430!important;font-size:22px!important;font-weight:700!important;
                   margin:0;letter-spacing:-0.3px;">
            ICT Risk Management Platform
        </h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="border-top:2px solid #1F3A5F;margin:14px 0 0 0;"></div>
<div style="border-top:1px solid #D9E1EA;margin:0 0 28px 0;"></div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Introduzione
# ---------------------------------------------------------------------------
st.markdown("""
<p style="color:#5B6573;font-size:14px;max-width:680px;line-height:1.75;margin-bottom:36px;">
    Piattaforma per la <strong style="color:#1B2430;font-weight:600;">valutazione del rischio ICT</strong>
    e la due diligence dei fornitori di servizi tecnologici, in conformità con il
    <strong style="color:#1B2430;font-weight:600;">Regolamento DORA (UE 2022/2554)</strong>
    e le linee guida EBA/BCE per istituti bancari e
    intermediari finanziari ex art. 106 del TUB.
</p>
""", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Dashboard cards
# ---------------------------------------------------------------------------
def render_dashboard_cards() -> None:
    col1, col2, col3 = st.columns(3, gap="large")

    cards = [
        {
            "col":     col1,
            "num":     "01",
            "tag":     "Rischio Inerente ICT",
            "title":   "Questionario Rischio ICT",
            "desc":    (
                "Valutazione del rischio inerente dei servizi TIC: "
                "disponibilità e continuità operativa, sicurezza ICT, "
                "gestione dei cambiamenti e integrità dei dati. "
                "Quattro scenari operativi differenziati."
            ),
            "cta":     "Avvia valutazione →",
            "link":    "pages/1_Questionario_Rischio_ICT.py",
            "accent":  "#1F3A5F",
            "tag_c":   "#1F3A5F",
        },
        {
            "col":     col2,
            "num":     "02",
            "tag":     "Sicurezza ICT Fornitori",
            "title":   "Questionario Sicurezza Fornitori",
            "desc":    (
                "Analisi delle misure di sicurezza dei fornitori TIC: "
                "certificazioni (ISO 27001, SOC 2), governance, "
                "continuità operativa, IAM, vulnerability management "
                "e gestione della supply chain."
            ),
            "cta":     "Avvia valutazione →",
            "link":    "pages/2_Questionario_Sicurezza_ICT_Fornitori.py",
            "accent":  "#2E6F6D",
            "tag_c":   "#2E6F6D",
        },
        {
            "col":     col3,
            "num":     "03",
            "tag":     "Rischio Residuo",
            "title":   "Registro Rischi",
            "desc":    (
                "Riepilogo consolidato del rischio residuo per tutti i "
                "servizi TIC valutati. Matrice di incrocio DORA-compliant, "
                "collegamento Q1–Q2 e reportistica Excel per il "
                "management reporting."
            ),
            "cta":     "Apri registro →",
            "link":    "pages/3_Registro_Rischi.py",
            "accent":  "#4F6B8A",
            "tag_c":   "#4F6B8A",
        },
    ]

    for card in cards:
        with card["col"]:
            st.markdown(f"""
            <div style="
                background:#FFFFFF;
                border:1px solid #D9E1EA;
                border-top:3px solid {card['accent']};
                border-radius:6px;
                padding:26px 24px 22px 24px;
                box-shadow:0 2px 8px rgba(21,37,53,0.05);
                min-height:230px;
            ">
                <div style="display:flex;align-items:center;
                            justify-content:space-between;margin-bottom:14px;">
                    <span style="color:{card['tag_c']};font-size:10px;font-weight:700;
                                 text-transform:uppercase;letter-spacing:1.4px;">
                        {card['tag']}
                    </span>
                    <span style="color:#D9E1EA;font-size:18px;font-weight:700;
                                 letter-spacing:-1px;">
                        {card['num']}
                    </span>
                </div>
                <h3 style="color:#1B2430!important;font-size:15px!important;
                           font-weight:700!important;margin:0 0 10px 0;
                           line-height:1.3;">
                    {card['title']}
                </h3>
                <p style="color:#5B6573!important;font-size:12.5px!important;
                          line-height:1.65!important;margin:0;">
                    {card['desc']}
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
            st.page_link(card["link"], label=card["cta"], use_container_width=True)


render_dashboard_cards()

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="border-top:1px solid #D9E1EA;padding-top:18px;margin-top:12px;">
    <p style="color:#C0CAD4;font-size:11px;margin:0;line-height:1.6;">
        © 2025 Meta Advisory & Tech Services S.r.l. &nbsp;·&nbsp;
        ICT Risk Management Platform &nbsp;·&nbsp;
        Conforme DORA (UE 2022/2554) &nbsp;·&nbsp;
        Uso riservato &nbsp;·&nbsp; v1.0
    </p>
</div>
""", unsafe_allow_html=True)
