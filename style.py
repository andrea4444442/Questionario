"""
Tema grafico enterprise — ICT Risk Management Platform.
Palette istituzionale: navy scuro · grigio neutro · accenti teal controllati.
"""
import streamlit as st
import streamlit.components.v1 as _components

# ---------------------------------------------------------------------------
# Palette di riferimento
# ---------------------------------------------------------------------------
C = {
    "bg":           "#F5F7FA",
    "surface":      "#FFFFFF",
    "sidebar":      "#152535",
    "sidebar_2":    "#1C3246",
    "primary":      "#1F3A5F",
    "primary_h":    "#16314F",
    "accent":       "#2E6F6D",
    "accent_2":     "#4F6B8A",
    "border":       "#D9E1EA",
    "border_2":     "#EBF0F6",
    "text_1":       "#1B2430",
    "text_2":       "#5B6573",
    "text_3":       "#8E97A3",
    "success_soft": "#DCEFE8",
    "warning_soft": "#F6EEDB",
    "danger_soft":  "#F5E2E2",
}

# ---------------------------------------------------------------------------
# CSS globale
# ---------------------------------------------------------------------------
_CSS = """
<style>
/* ── FONT ─────────────────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

*, *::before, *::after {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
}

/*
   FIX CRITICO: il selettore * con !important sovrascriveva il font
   Material Icons di Streamlit, rendendo le icone come testo
   (es. "keyboard_double_arrow_left"). Re-applichiamo il font corretto
   su tutte le classi Material Icons.
*/
.material-icons,
.material-icons-sharp,
.material-icons-outlined,
.material-icons-round,
.material-symbols-rounded,
.material-symbols-outlined,
.material-symbols-sharp,
span[class*="material"] {
    font-family: 'Material Icons Sharp', 'Material Icons Outlined',
                 'Material Icons Round', 'Material Icons',
                 'Material Symbols Rounded' !important;
    font-size: 20px !important;
    line-height: 1 !important;
    display: inline-flex !important;
    align-items: center !important;
}

/* ── SIDEBAR TOGGLE BUTTON (hamburger) ──────────────────────────────── */
[data-testid="stSidebarCollapsedControl"] {
    background: #FFFFFF !important;
    border-right: 1px solid #D9E1EA !important;
}
[data-testid="stSidebarCollapsedControl"] button {
    background: transparent !important;
    border: none !important;
    border-radius: 4px !important;
    width: 36px !important;
    height: 36px !important;
    padding: 0 !important;
    margin: 10px 6px !important;
    cursor: pointer !important;
    transition: background 0.15s !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
}
[data-testid="stSidebarCollapsedControl"] button:hover {
    background: #EDF0F5 !important;
}
/*
   APPROCCIO DEFINITIVO — font-size:0 su tutti i discendenti.
   Nasconde qualsiasi testo/icona dentro il bottone (testo Material Icons,
   SVG, span con qualunque classe) indipendentemente dalla struttura DOM
   della versione di Streamlit in uso.
*/
[data-testid="stSidebarCollapsedControl"] * {
    font-size: 0 !important;
    line-height: 0 !important;
    color: transparent !important;
}
[data-testid="stSidebarCollapsedControl"] svg {
    display: none !important;
}
/*
   Mostra ☰ tramite ::after con font-size esplicita.
   ::after è generato da CSS, non è un discendente DOM,
   quindi NON eredita font-size:0 dai figli sopra.
*/
[data-testid="stSidebarCollapsedControl"] button {
    position: relative !important;
    overflow: visible !important;
    width: 36px !important;
    height: 36px !important;
    background: transparent !important;
    border: none !important;
    cursor: pointer !important;
    border-radius: 4px !important;
}
[data-testid="stSidebarCollapsedControl"] button:hover {
    background: #EDF0F5 !important;
}
[data-testid="stSidebarCollapsedControl"] button::after {
    content: "☰" !important;
    font-family: Arial, Helvetica, sans-serif !important;
    font-size: 20px !important;
    font-weight: 400 !important;
    line-height: 1 !important;
    color: #5B6573 !important;
    position: absolute !important;
    top: 50% !important;
    left: 50% !important;
    transform: translate(-50%, -50%) !important;
    display: block !important;
}

/* ── SIDEBAR CLOSE BUTTON (dentro la sidebar aperta) ────────────────── */
section[data-testid="stSidebar"] [data-testid="stBaseButton-headerNoPadding"] {
    background: transparent !important;
    border: none !important;
    border-radius: 4px !important;
    padding: 6px !important;
    transition: background 0.15s !important;
    position: relative !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    min-width: 28px !important;
    min-height: 28px !important;
}
section[data-testid="stSidebar"] [data-testid="stBaseButton-headerNoPadding"]:hover {
    background: rgba(255,255,255,0.08) !important;
}
/* Nasconde contenuto originale del bottone chiudi sidebar */
section[data-testid="stSidebar"] [data-testid="stBaseButton-headerNoPadding"] > *,
section[data-testid="stSidebar"] [data-testid="stBaseButton-headerNoPadding"] span,
section[data-testid="stSidebar"] [data-testid="stBaseButton-headerNoPadding"] svg {
    opacity: 0 !important;
    position: absolute !important;
    pointer-events: none !important;
}
/* Inietta ✕ tramite ::after centrato */
section[data-testid="stSidebar"] [data-testid="stBaseButton-headerNoPadding"]::after {
    content: "✕" !important;
    font-family: Arial, Helvetica, sans-serif !important;
    font-size: 13px !important;
    font-weight: 400 !important;
    color: #7A9AB0 !important;
    position: absolute !important;
    top: 50% !important;
    left: 50% !important;
    transform: translate(-50%, -50%) !important;
    display: block !important;
    line-height: 1 !important;
    opacity: 1 !important;
    pointer-events: none !important;
}

/* ── SIDEBAR NAV AUTOMATICA (duplicata) — nascosta ───────────────────── */
/*
   Streamlit genera automaticamente una sezione di navigazione in sidebar
   basata sui file in pages/. Poiché la navigazione personalizzata in
   render_sidebar() già copre tutti i link, quella auto-generata va nascosta.
*/
[data-testid="stSidebarNav"],
[data-testid="stSidebarNavItems"],
section[data-testid="stSidebar"] nav {
    display: none !important;
}

/* ── APP BACKGROUND ──────────────────────────────────────────────────── */
.stApp { background-color: #F5F7FA !important; }

.main .block-container {
    padding: 2.5rem 3rem 4rem 3rem !important;
    max-width: 1180px !important;
}

/* ── STREAMLIT TOP BAR ───────────────────────────────────────────────── */
header[data-testid="stHeader"] {
    background-color: #FFFFFF !important;
    border-bottom: 1px solid #D9E1EA !important;
    height: 3px !important;
}

/* ── SIDEBAR ─────────────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background-color: #152535 !important;
    border-right: 1px solid #0D1E2C !important;
}
[data-testid="stSidebar"] > div:first-child {
    background-color: #152535 !important;
    padding-top: 0 !important;
}
[data-testid="stSidebar"] * { color: #A8BCC8 !important; }
[data-testid="stSidebar"] strong { color: #FFFFFF !important; }
[data-testid="stSidebar"] hr {
    border-top: 1px solid #1F3A5F !important;
    margin: 12px 0 !important;
}

/* Sidebar — nav page links */
[data-testid="stSidebar"] [data-testid="stPageLink"] > a {
    background: transparent !important;
    color: #7A9AB0 !important;
    font-size: 13px !important;
    font-weight: 400 !important;
    padding: 8px 12px !important;
    border-radius: 4px !important;
    text-align: left !important;
    display: block !important;
    text-decoration: none !important;
    border: none !important;
    transition: background 0.15s, color 0.15s !important;
}
[data-testid="stSidebar"] [data-testid="stPageLink"] > a:hover {
    background: rgba(255,255,255,0.07) !important;
    color: #FFFFFF !important;
}

/* Sidebar — logout button */
[data-testid="stSidebar"] .stButton > button {
    background: transparent !important;
    border: 1px solid #2A4560 !important;
    color: #7A9AB0 !important;
    font-size: 12px !important;
    font-weight: 500 !important;
    padding: 7px 14px !important;
    border-radius: 4px !important;
    width: 100% !important;
    letter-spacing: 0.2px !important;
    transition: all 0.15s !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(255,255,255,0.06) !important;
    border-color: #4F6B8A !important;
    color: #FFFFFF !important;
}

/* ── TYPOGRAPHY ──────────────────────────────────────────────────────── */
h1 {
    color: #1B2430 !important;
    font-size: 22px !important;
    font-weight: 700 !important;
    letter-spacing: -0.3px !important;
    line-height: 1.3 !important;
    margin-bottom: 4px !important;
}
h2 {
    color: #1B2430 !important;
    font-size: 17px !important;
    font-weight: 600 !important;
    letter-spacing: -0.2px !important;
}
h3 {
    color: #1B2430 !important;
    font-size: 14px !important;
    font-weight: 600 !important;
}

/* ── BUTTONS (content area) ──────────────────────────────────────────── */
.main .stButton > button {
    background-color: #1F3A5F !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 4px !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    padding: 9px 22px !important;
    letter-spacing: 0.2px !important;
    transition: background-color 0.18s, box-shadow 0.18s !important;
    box-shadow: 0 1px 3px rgba(31,58,95,0.18) !important;
}
.main .stButton > button:hover {
    background-color: #16314F !important;
    box-shadow: 0 3px 10px rgba(31,58,95,0.22) !important;
}

/* ── SECONDARY BUTTON (pulsante ⓘ info card) ────────────────────────── */
.main .stButton > button[kind="secondary"] {
    background: transparent !important;
    border: 1.5px solid #D9E1EA !important;
    color: #5B6573 !important;
    border-radius: 4px !important;
    font-size: 15px !important;
    font-weight: 400 !important;
    padding: 4px 8px !important;
    box-shadow: none !important;
    transition: all 0.15s !important;
}
.main .stButton > button[kind="secondary"]:hover {
    border-color: #1F3A5F !important;
    color: #1F3A5F !important;
    background: #F0F4FA !important;
}

/* ── DOWNLOAD BUTTON ─────────────────────────────────────────────────── */
.stDownloadButton > button {
    background-color: #FFFFFF !important;
    color: #1F3A5F !important;
    border: 1.5px solid #D9E1EA !important;
    border-radius: 4px !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    padding: 8px 18px !important;
    transition: all 0.15s !important;
}
.stDownloadButton > button:hover {
    border-color: #1F3A5F !important;
    background-color: #F0F4FA !important;
}

/* ── PAGE LINKS (content area) ───────────────────────────────────────── */
.main [data-testid="stPageLink"] > a {
    background-color: #1F3A5F !important;
    color: #FFFFFF !important;
    border-radius: 4px !important;
    padding: 9px 20px !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    text-align: center !important;
    text-decoration: none !important;
    display: block !important;
    transition: background-color 0.18s !important;
    letter-spacing: 0.2px !important;
    border: none !important;
    box-shadow: 0 1px 3px rgba(31,58,95,0.18) !important;
}
.main [data-testid="stPageLink"] > a:hover {
    background-color: #16314F !important;
}

/* ── INPUTS ──────────────────────────────────────────────────────────── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stNumberInput > div > div > input {
    background-color: #FFFFFF !important;
    border: 1px solid #D9E1EA !important;
    border-radius: 4px !important;
    color: #1B2430 !important;
    font-size: 14px !important;
    padding: 9px 12px !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus,
.stNumberInput > div > div > input:focus {
    border-color: #1F3A5F !important;
    box-shadow: 0 0 0 3px rgba(31,58,95,0.08) !important;
    outline: none !important;
}

/* Selectbox */
.stSelectbox [data-baseweb="select"] > div:first-child {
    border: 1px solid #D9E1EA !important;
    border-radius: 4px !important;
    background-color: #FFFFFF !important;
    font-size: 14px !important;
}

/* Multiselect */
.stMultiSelect [data-baseweb="select"] > div:first-child {
    border: 1px solid #D9E1EA !important;
    border-radius: 4px !important;
    background-color: #FFFFFF !important;
}

/* File uploader */
[data-testid="stFileUploader"] {
    border: 1.5px dashed #D9E1EA !important;
    border-radius: 6px !important;
    background: #FAFBFD !important;
}

/* ── FORM CONTAINER ──────────────────────────────────────────────────── */
[data-testid="stForm"] {
    border: 1px solid #D9E1EA !important;
    border-radius: 6px !important;
    padding: 20px 24px !important;
    background: #FFFFFF !important;
}

/* ── DIVIDER ─────────────────────────────────────────────────────────── */
hr {
    border: none !important;
    border-top: 1px solid #D9E1EA !important;
    margin: 16px 0 !important;
}

/* ── METRICS ─────────────────────────────────────────────────────────── */
[data-testid="stMetric"] {
    background: #FFFFFF !important;
    padding: 20px 18px !important;
    border-radius: 6px !important;
    border: 1px solid #D9E1EA !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.04) !important;
}
[data-testid="stMetricLabel"] {
    color: #5B6573 !important;
    font-size: 11px !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.6px !important;
}
[data-testid="stMetricValue"] {
    color: #1B2430 !important;
    font-weight: 700 !important;
}

/* ── ALERTS ──────────────────────────────────────────────────────────── */
.stAlert { border-radius: 4px !important; font-size: 13px !important; }

/* ── RADIO ───────────────────────────────────────────────────────────── */
.stRadio > label {
    color: #1B2430 !important;
    font-size: 14px !important;
    font-weight: 500 !important;
}

/* ── SUBHEADER ───────────────────────────────────────────────────────── */
[data-testid="stMarkdownContainer"] h3 { color: #1B2430 !important; }

/* ── FILE UPLOADER ───────────────────────────────────────────────────── */
[data-testid="stFileUploaderDropzone"] {
    background: #FAFBFD !important;
    border: 1.5px dashed #C8D4DF !important;
    border-radius: 6px !important;
    padding: 20px !important;
    transition: border-color 0.2s, background 0.2s !important;
}
[data-testid="stFileUploaderDropzone"]:hover {
    border-color: #1F3A5F !important;
    background: #F0F4FA !important;
}
[data-testid="stFileUploaderDropzoneInstructions"] > div > span {
    color: #5B6573 !important;
    font-size: 13px !important;
    font-weight: 500 !important;
}
[data-testid="stFileUploaderDropzoneInstructions"] > div > small {
    color: #8E97A3 !important;
    font-size: 11px !important;
}
/* Bottone "Browse files" */
[data-testid="stFileUploaderDropzone"] button {
    background: #1F3A5F !important;
    color: #FFFFFF !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    border-radius: 4px !important;
    padding: 7px 16px !important;
    border: none !important;
    letter-spacing: 0.2px !important;
    transition: background 0.15s !important;
}
[data-testid="stFileUploaderDropzone"] button:hover {
    background: #16314F !important;
}
/* File allegato (dopo upload) */
[data-testid="stFileUploaderFile"] {
    background: #F0F4FA !important;
    border: 1px solid #D9E1EA !important;
    border-radius: 4px !important;
    padding: 8px 12px !important;
    font-size: 13px !important;
}

/* ── SCROLLBAR ───────────────────────────────────────────────────────── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: #F5F7FA; }
::-webkit-scrollbar-thumb { background: #C8D4DF; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #9AAAB8; }
</style>
"""


_HAMBURGER_JS = """
<script>
(function() {
    function fixHamburger() {
        var doc = window.parent.document;
        if (!doc) return;
        // Targetta SOLO il container del toggle collassato, non i bottoni dentro la sidebar aperta
        var containers = doc.querySelectorAll('[data-testid="stSidebarCollapsedControl"]');
        containers.forEach(function(container) {
            var btn = container.querySelector('button');
            if (!btn) return;
            if (!btn.getAttribute('data-h-fixed')) {
                btn.setAttribute('data-h-fixed', '1');
                btn.style.cssText += 'font-size:0!important;color:transparent!important;position:relative!important;overflow:visible!important;';
                var spans = btn.querySelectorAll('span');
                spans.forEach(function(s){ s.style.cssText += 'font-size:0!important;opacity:0!important;'; });
            }
            // Aggiorna sempre la visibilità dell'icona: mostra ☰ solo se sidebar chiusa
            var existing = btn.querySelector('[data-hamburger]');
            var sidebarOpen = !!doc.querySelector('[data-testid="stSidebar"][aria-expanded="true"]')
                           || !!doc.querySelector('[data-testid="stSidebar"].st-emotion-cache-1cypcdb')
                           || (doc.querySelector('[data-testid="stSidebar"]') &&
                               doc.querySelector('[data-testid="stSidebar"]').style.display !== 'none' &&
                               getComputedStyle(doc.querySelector('[data-testid="stSidebar"]')).width !== '0px');
            if (!existing) {
                var icon = doc.createElement('span');
                icon.setAttribute('data-hamburger', '1');
                icon.textContent = '☰';
                icon.style.cssText = 'font-size:20px!important;color:#5B6573!important;position:absolute!important;top:50%!important;left:50%!important;transform:translate(-50%,-50%)!important;line-height:1!important;font-family:Arial,Helvetica,sans-serif!important;pointer-events:none!important;opacity:1!important;';
                btn.appendChild(icon);
                existing = icon;
            }
            existing.style.opacity = sidebarOpen ? '0' : '1';
        });
    }
    setTimeout(fixHamburger, 200);
    setTimeout(fixHamburger, 800);
    var observer = new MutationObserver(function(){ fixHamburger(); });
    observer.observe(window.parent.document.body, {childList:true, subtree:true, attributes:true});
})();
</script>
"""


def apply_custom_theme() -> None:
    """Inietta il CSS globale e il JS per l'hamburger. Da chiamare all'inizio di ogni pagina."""
    st.markdown(_CSS, unsafe_allow_html=True)
    _components.html(_HAMBURGER_JS, height=0, scrolling=False)


# Alias per compatibilità con il codice esistente
inject_css = apply_custom_theme


def render_sidebar(current_page: str = "") -> None:
    """Sidebar di navigazione professionale con stato sessione e logout."""
    with st.sidebar:
        # Brand header
        st.markdown(f"""
        <div style="padding:28px 20px 20px 20px; border-bottom:1px solid #1F3A5F;">
            <p style="color:#4F7A8A!important; font-size:10px; font-weight:600;
                      text-transform:uppercase; letter-spacing:1.8px; margin:0 0 6px 0;">
                Meta Advisory
            </p>
            <p style="color:#FFFFFF!important; font-size:15px; font-weight:700;
                      margin:0; letter-spacing:-0.2px;">
                ICT Risk Platform
            </p>
            {"<p style='color:#4F7A8A!important;font-size:11px;margin:8px 0 0 0;'>"+current_page+"</p>" if current_page else ""}
        </div>
        """, unsafe_allow_html=True)

        # Navigazione
        st.markdown("""
        <p style="color:#4F6B8A!important; font-size:10px; font-weight:600;
                  text-transform:uppercase; letter-spacing:1.4px;
                  padding:20px 20px 6px 20px; margin:0;">
            Navigazione
        </p>
        """, unsafe_allow_html=True)

        st.page_link("app.py",                                          label="  Dashboard",              icon="▪")
        st.page_link("pages/1_Questionario_Rischio_ICT.py",             label="  Questionario Rischio ICT", icon="▪")
        st.page_link("pages/2_Questionario_Sicurezza_ICT_Fornitori.py", label="  Sicurezza Fornitori",    icon="▪")
        st.page_link("pages/3_Registro_Rischi.py",                      label="  Registro Rischi",        icon="▪")

        # Spacer + sessione + logout
        st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("""
        <div style="padding:0 20px 8px 20px;">
            <p style="color:#4F6B8A!important;font-size:10px;text-transform:uppercase;
                      letter-spacing:1px;margin:0 0 2px 0;">Sessione attiva</p>
            <p style="color:#A8BCC8!important;font-size:13px;font-weight:500;margin:0;">admin</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Esci dalla piattaforma", key="__logout__"):
            st.session_state["logged_in"] = False
            st.rerun()


def page_header(title: str, subtitle: str = "", tag: str = "") -> None:
    """Header di sezione con tag, titolo e sottotitolo."""
    tag_html = f'<p style="color:#4F6B8A;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:1.4px;margin:0 0 6px 0;">{tag}</p>' if tag else ""
    sub_html  = f'<p style="color:#5B6573;font-size:13px;margin:4px 0 0 0;line-height:1.6;">{subtitle}</p>' if subtitle else ""
    st.markdown(f"""
    <div style="margin-bottom:28px;">
        {tag_html}
        <h1 style="color:#1B2430!important;margin:0;">{title}</h1>
        {sub_html}
        <div style="width:36px;height:3px;background:#1F3A5F;border-radius:2px;margin-top:12px;"></div>
    </div>
    """, unsafe_allow_html=True)
