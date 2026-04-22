import streamlit as st
import os
from auth import require_login
from style import apply_custom_theme, render_sidebar

st.set_page_config(
    page_title="ICT Risk Platform — Meta Advisory",
    page_icon="▪",
    layout="wide",
    initial_sidebar_state="collapsed",
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
# Info modali — @st.dialog (Streamlit >= 1.36)
# Ogni funzione viene chiamata quando l'utente clicca il pulsante info
# della card corrispondente. Streamlit gestisce l'overlay automaticamente.
# ---------------------------------------------------------------------------

@st.dialog("Questionario Rischio ICT — Dettaglio")
def _dlg_q1() -> None:
    st.markdown(
        "<p style='color:#5B6573;font-size:13px;line-height:1.75;margin:0 0 14px 0;'>"
        "Il <strong style='color:#1B2430;'>Questionario Rischio ICT</strong> valuta il "
        "<strong>rischio inerente</strong> dei servizi TIC critici in conformità con "
        "il Regolamento DORA (UE 2022/2554) e le linee guida EBA/BCE.</p>"
        "<p style='color:#1F3A5F;font-size:10px;font-weight:700;text-transform:uppercase;"
        "letter-spacing:1.3px;margin:0 0 8px 0;'>Aree di valutazione</p>"
        "<ul style='color:#5B6573;font-size:13px;line-height:1.85;padding-left:18px;margin:0 0 14px 0;'>"
        "<li><strong style='color:#1B2430;'>Disponibilità e continuità operativa</strong>"
        " — RTO/RPO, ridondanza, failover</li>"
        "<li><strong style='color:#1B2430;'>Sicurezza ICT</strong>"
        " — controlli tecnici, crittografia, accessi privilegiati</li>"
        "<li><strong style='color:#1B2430;'>Gestione dei cambiamenti</strong>"
        " — patch management, release management</li>"
        "<li><strong style='color:#1B2430;'>Integrità dei dati</strong>"
        " — backup, data loss prevention, audit log</li>"
        "</ul>"
        "<p style='color:#1F3A5F;font-size:10px;font-weight:700;text-transform:uppercase;"
        "letter-spacing:1.3px;margin:0 0 8px 0;'>Scenari operativi</p>"
        "<p style='color:#5B6573;font-size:13px;line-height:1.75;margin:0 0 14px 0;'>"
        "Differenzia quattro scenari (A–D) in base alla criticità del servizio e alla "
        "natura del fornitore: cloud, on-premise, ibrido, critico.</p>"
        "<div style='background:#F0F4FA;border-left:3px solid #1F3A5F;"
        "border-radius:0 4px 4px 0;padding:10px 14px;'>"
        "<p style='color:#1B2430;font-size:12px;font-weight:600;margin:0 0 4px 0;'>Output</p>"
        "<p style='color:#5B6573;font-size:12px;margin:0;line-height:1.6;'>"
        "Score di rischio inerente (Basso / Medio / Alto / Critico), "
        "PDF di dettaglio, salvataggio automatico su Registro Rischi.</p></div>",
        unsafe_allow_html=True,
    )


@st.dialog("Questionario Sicurezza Fornitori — Dettaglio")
def _dlg_q2() -> None:
    st.markdown(
        "<p style='color:#5B6573;font-size:13px;line-height:1.75;margin:0 0 14px 0;'>"
        "Il <strong style='color:#1B2430;'>Questionario Sicurezza Fornitori</strong> analizza "
        "le misure di sicurezza adottate dai fornitori TIC secondo i requisiti "
        "DORA Artt. 28–30 e le linee guida EBA sul rischio ICT di terze parti.</p>"
        "<p style='color:#2E6F6D;font-size:10px;font-weight:700;text-transform:uppercase;"
        "letter-spacing:1.3px;margin:0 0 8px 0;'>Sezioni del questionario</p>"
        "<ul style='color:#5B6573;font-size:13px;line-height:1.85;padding-left:18px;margin:0 0 14px 0;'>"
        "<li><strong style='color:#1B2430;'>Certificazioni</strong>"
        " — ISO 27001, SOC 2 Type II, ISO 22301, PCI-DSS</li>"
        "<li><strong style='color:#1B2430;'>Governance della sicurezza</strong>"
        " — policy, CISO, security awareness</li>"
        "<li><strong style='color:#1B2430;'>Identity &amp; Access Management</strong>"
        " — MFA, PAM, RBAC, zero trust</li>"
        "<li><strong style='color:#1B2430;'>Vulnerability Management</strong>"
        " — SAST/DAST, penetration testing, patching SLA</li>"
        "<li><strong style='color:#1B2430;'>Continuità operativa</strong>"
        " — BCP, DRP, test di failover documentati</li>"
        "<li><strong style='color:#1B2430;'>Supply chain security</strong>"
        " — SBOM, vetting subfornitori, controlli quarte parti</li>"
        "</ul>"
        "<div style='background:#F0F8F7;border-left:3px solid #2E6F6D;"
        "border-radius:0 4px 4px 0;padding:10px 14px;'>"
        "<p style='color:#1B2430;font-size:12px;font-weight:600;margin:0 0 4px 0;'>Output</p>"
        "<p style='color:#5B6573;font-size:12px;margin:0;line-height:1.6;'>"
        "Punteggio misure di sicurezza (Adeguate / Parziali / Inadeguate), "
        "PDF allegabile alla due diligence, collegamento automatico al Registro Rischi.</p></div>",
        unsafe_allow_html=True,
    )


@st.dialog("Registro Rischi — Dettaglio")
def _dlg_q3() -> None:
    st.markdown(
        "<p style='color:#5B6573;font-size:13px;line-height:1.75;margin:0 0 14px 0;'>"
        "Il <strong style='color:#1B2430;'>Registro Rischi</strong> è il punto di convergenza "
        "dei risultati di Q1 e Q2: calcola il <strong>rischio residuo</strong> per ciascun "
        "servizio TIC e produce la reportistica per il management reporting DORA.</p>"
        "<p style='color:#4F6B8A;font-size:10px;font-weight:700;text-transform:uppercase;"
        "letter-spacing:1.3px;margin:0 0 8px 0;'>Funzionalità principali</p>"
        "<ul style='color:#5B6573;font-size:13px;line-height:1.85;padding-left:18px;margin:0 0 14px 0;'>"
        "<li><strong style='color:#1B2430;'>Matrice di incrocio DORA-compliant</strong>"
        " — rischio inerente × misure di sicurezza</li>"
        "<li><strong style='color:#1B2430;'>Collegamento Q1–Q2</strong>"
        " — mapping automatico per nome servizio ICT</li>"
        "<li><strong style='color:#1B2430;'>Risk scoring residuo</strong>"
        " — Basso / Medio / Medio Alto / Alto / Critico</li>"
        "<li><strong style='color:#1B2430;'>Export Excel</strong>"
        " — report per CRO, CIO, Board e Autorità di vigilanza</li>"
        "<li><strong style='color:#1B2430;'>Storico valutazioni</strong>"
        " — tracciabilità completa per audit trail</li>"
        "</ul>"
        "<div style='background:#F0F4FA;border-left:3px solid #4F6B8A;"
        "border-radius:0 4px 4px 0;padding:10px 14px;'>"
        "<p style='color:#1B2430;font-size:12px;font-weight:600;margin:0 0 4px 0;'>Conformità normativa</p>"
        "<p style='color:#5B6573;font-size:12px;margin:0;line-height:1.6;'>"
        "Output conforme ai requisiti DORA Art. 28–30, EBA/GL/2019/04 "
        "e aspettative di supervisione BCE/Banca d'Italia.</p></div>",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Dashboard cards
# ---------------------------------------------------------------------------
# NOTA TECNICA: il markup delle card usa concatenazione di f-string (non
# un singolo blocco multi-riga) per evitare che l'indentazione Python venga
# interpretata come code block dal parser markdown di Streamlit (4+ spazi
# all'inizio di una riga = code block in CommonMark).
# ---------------------------------------------------------------------------

_MODAL_BODY_OBSOLETO = {
    "01": """
        <p style="color:#5B6573;font-size:13px;line-height:1.75;margin:0 0 16px 0;">
            Il <strong style="color:#1B2430;">Questionario Rischio ICT</strong> valuta il
            <strong>rischio inerente</strong> associato ai servizi TIC critici, in linea con
            i requisiti del Regolamento DORA (UE 2022/2554) e le linee guida EBA/BCE.
        </p>
        <p style="color:#1F3A5F;font-size:10px;font-weight:700;text-transform:uppercase;
                  letter-spacing:1.3px;margin:0 0 8px 0;">Aree di valutazione</p>
        <ul style="color:#5B6573;font-size:13px;line-height:1.85;padding-left:18px;margin:0 0 16px 0;">
            <li><strong style="color:#1B2430;">Disponibilità e continuità operativa</strong>
                — RTO/RPO, ridondanza, failover</li>
            <li><strong style="color:#1B2430;">Sicurezza ICT</strong>
                — controlli tecnici, crittografia, accessi privilegiati</li>
            <li><strong style="color:#1B2430;">Gestione dei cambiamenti</strong>
                — patch management, release management</li>
            <li><strong style="color:#1B2430;">Integrità dei dati</strong>
                — backup, data loss prevention, audit log</li>
        </ul>
        <p style="color:#1F3A5F;font-size:10px;font-weight:700;text-transform:uppercase;
                  letter-spacing:1.3px;margin:0 0 8px 0;">Scenari operativi</p>
        <p style="color:#5B6573;font-size:13px;line-height:1.75;margin:0 0 16px 0;">
            Differenzia quattro scenari (A–D) in base alla criticità del servizio
            e alla natura del fornitore: cloud, on-premise, ibrido, critico.
        </p>
        <div style="background:#F0F4FA;border-left:3px solid #1F3A5F;
                    border-radius:0 4px 4px 0;padding:10px 14px;">
            <p style="color:#1B2430;font-size:12px;font-weight:600;margin:0 0 4px 0;">Output</p>
            <p style="color:#5B6573;font-size:12px;margin:0;line-height:1.6;">
                Score di rischio inerente (Basso / Medio / Alto / Critico),
                PDF di dettaglio, salvataggio automatico su Registro Rischi.
            </p>
        </div>
    """,
    "02": """
        <p style="color:#5B6573;font-size:13px;line-height:1.75;margin:0 0 16px 0;">
            Il <strong style="color:#1B2430;">Questionario Sicurezza Fornitori</strong> analizza
            le misure di sicurezza adottate dai fornitori TIC, secondo i requisiti DORA
            Artt. 28–30 e le linee guida EBA sul rischio ICT di terze parti.
        </p>
        <p style="color:#2E6F6D;font-size:10px;font-weight:700;text-transform:uppercase;
                  letter-spacing:1.3px;margin:0 0 8px 0;">Sezioni del questionario</p>
        <ul style="color:#5B6573;font-size:13px;line-height:1.85;padding-left:18px;margin:0 0 16px 0;">
            <li><strong style="color:#1B2430;">Certificazioni</strong>
                — ISO 27001, SOC 2 Type II, ISO 22301, PCI-DSS</li>
            <li><strong style="color:#1B2430;">Governance della sicurezza</strong>
                — policy, CISO, security awareness</li>
            <li><strong style="color:#1B2430;">Identity &amp; Access Management</strong>
                — MFA, PAM, RBAC, zero trust</li>
            <li><strong style="color:#1B2430;">Vulnerability Management</strong>
                — SAST/DAST, penetration testing, patching SLA</li>
            <li><strong style="color:#1B2430;">Continuità operativa</strong>
                — BCP, DRP, test di failover documentati</li>
            <li><strong style="color:#1B2430;">Supply chain security</strong>
                — SBOM, vetting subfornitori, controlli quarte parti</li>
        </ul>
        <div style="background:#F0F8F7;border-left:3px solid #2E6F6D;
                    border-radius:0 4px 4px 0;padding:10px 14px;">
            <p style="color:#1B2430;font-size:12px;font-weight:600;margin:0 0 4px 0;">Output</p>
            <p style="color:#5B6573;font-size:12px;margin:0;line-height:1.6;">
                Punteggio misure di sicurezza (Adeguate / Parziali / Inadeguate),
                PDF allegabile alla due diligence, collegamento automatico al Registro Rischi.
            </p>
        </div>
    """,
    "03": """
        <p style="color:#5B6573;font-size:13px;line-height:1.75;margin:0 0 16px 0;">
            Il <strong style="color:#1B2430;">Registro Rischi</strong> è il punto di convergenza
            dei risultati di Q1 e Q2: calcola il <strong>rischio residuo</strong> per ciascun
            servizio TIC valutato e produce la reportistica per il management reporting DORA.
        </p>
        <p style="color:#4F6B8A;font-size:10px;font-weight:700;text-transform:uppercase;
                  letter-spacing:1.3px;margin:0 0 8px 0;">Funzionalità principali</p>
        <ul style="color:#5B6573;font-size:13px;line-height:1.85;padding-left:18px;margin:0 0 16px 0;">
            <li><strong style="color:#1B2430;">Matrice di incrocio DORA-compliant</strong>
                — rischio inerente × misure di sicurezza</li>
            <li><strong style="color:#1B2430;">Collegamento Q1–Q2</strong>
                — mapping automatico per nome servizio ICT</li>
            <li><strong style="color:#1B2430;">Risk scoring residuo</strong>
                — Basso / Medio / Medio Alto / Alto / Critico</li>
            <li><strong style="color:#1B2430;">Export Excel</strong>
                — report per CRO, CIO, Board e Autorità di vigilanza</li>
            <li><strong style="color:#1B2430;">Storico valutazioni</strong>
                — tracciabilità completa per audit trail</li>
        </ul>
        <div style="background:#F0F4FA;border-left:3px solid #4F6B8A;
                    border-radius:0 4px 4px 0;padding:10px 14px;">
            <p style="color:#1B2430;font-size:12px;font-weight:600;margin:0 0 4px 0;">Conformità normativa</p>
            <p style="color:#5B6573;font-size:12px;margin:0;line-height:1.6;">
                Output conforme ai requisiti DORA Art. 28–30,
                EBA/GL/2019/04 e aspettative di supervisione BCE/Banca d'Italia.
            </p>
        </div>
    """,
}


# ---------------------------------------------------------------------------
# Dashboard cards
# ---------------------------------------------------------------------------
def render_dashboard_cards() -> None:
    col1, col2, col3 = st.columns(3, gap="large")

    cards = [
        {
            "col":    col1,
            "num":    "01",
            "tag":    "Rischio Inerente ICT",
            "title":  "Questionario Rischio ICT",
            "desc":   (
                "Valutazione del rischio inerente dei servizi TIC: "
                "disponibilità e continuità operativa, sicurezza ICT, "
                "gestione dei cambiamenti e integrità dei dati. "
                "Quattro scenari operativi differenziati."
            ),
            "cta":    "Avvia valutazione →",
            "link":   "pages/1_Questionario_Rischio_ICT.py",
            "accent": "#1F3A5F",
            "tag_c":  "#1F3A5F",
            "dlg":    _dlg_q1,
        },
        {
            "col":    col2,
            "num":    "02",
            "tag":    "Sicurezza ICT Fornitori",
            "title":  "Questionario Sicurezza Fornitori",
            "desc":   (
                "Analisi delle misure di sicurezza dei fornitori TIC: "
                "certificazioni (ISO 27001, SOC 2), governance, "
                "continuità operativa, IAM, vulnerability management "
                "e gestione della supply chain."
            ),
            "cta":    "Avvia valutazione →",
            "link":   "pages/2_Questionario_Sicurezza_ICT_Fornitori.py",
            "accent": "#2E6F6D",
            "tag_c":  "#2E6F6D",
            "dlg":    _dlg_q2,
        },
        {
            "col":    col3,
            "num":    "03",
            "tag":    "Rischio Residuo",
            "title":  "Registro Rischi",
            "desc":   (
                "Riepilogo consolidato del rischio residuo per tutti i "
                "servizi TIC valutati. Matrice di incrocio DORA-compliant, "
                "collegamento Q1–Q2 e reportistica Excel per il "
                "management reporting."
            ),
            "cta":    "Apri registro →",
            "link":   "pages/3_Registro_Rischi.py",
            "accent": "#4F6B8A",
            "tag_c":  "#4F6B8A",
            "dlg":    _dlg_q3,
        },
    ]

    for card in cards:
        with card["col"]:
            # L'f-string inizia con <div a colonna 0: obbligatorio per evitare che
            # il parser markdown di Streamlit interpreti l'indentazione come code block.
            st.markdown(
                f'<div style="background:#FFFFFF;border:1px solid #D9E1EA;'
                f'border-top:3px solid {card["accent"]};border-radius:6px;'
                f'padding:26px 24px 22px 24px;'
                f'box-shadow:0 2px 8px rgba(21,37,53,0.05);min-height:230px;">'
                f'<div style="display:flex;align-items:center;'
                f'justify-content:space-between;margin-bottom:14px;">'
                f'<span style="color:{card["tag_c"]};font-size:10px;font-weight:700;'
                f'text-transform:uppercase;letter-spacing:1.4px;">{card["tag"]}</span>'
                # Icona "i" decorativa — il pulsante cliccabile è lo st.button sotto
                f'<div style="display:flex;align-items:center;gap:8px;">'
                f'<span style="color:#D9E1EA;font-size:18px;font-weight:700;'
                f'letter-spacing:-1px;">{card["num"]}</span>'
                f'<span style="width:18px;height:18px;border-radius:50%;'
                f'border:1.5px solid {card["accent"]};color:{card["accent"]};'
                f'font-size:10px;font-weight:700;font-family:Inter,sans-serif;'
                f'display:inline-flex;align-items:center;justify-content:center;'
                f'line-height:1;user-select:none;" title="Clicca \'ⓘ\' per i dettagli">i</span>'
                f'</div></div>'
                f'<h3 style="color:#1B2430!important;font-size:15px!important;'
                f'font-weight:700!important;margin:0 0 10px 0;line-height:1.3;">'
                f'{card["title"]}</h3>'
                f'<p style="color:#5B6573!important;font-size:12.5px!important;'
                f'line-height:1.65!important;margin:0;">{card["desc"]}</p>'
                f'</div>',
                unsafe_allow_html=True,
            )

            st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

            # Riga bottom: pulsante info (sx, secondario) + CTA (dx, primario)
            info_c, cta_c = st.columns([1, 4])
            with info_c:
                if st.button("ⓘ", key=f"info_{card['num']}", use_container_width=True,
                             help="Dettagli modulo", type="secondary"):
                    card["dlg"]()
            with cta_c:
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
