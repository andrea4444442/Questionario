import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Font globale */
html, body, [class*="css"], .stApp {
    font-family: 'Inter', sans-serif !important;
}

/* Sfondo app */
.stApp {
    background-color: #F4F6FA;
}

/* Nascondi header Streamlit */
header[data-testid="stHeader"] {
    background-color: #00338D;
    height: 4px;
}

/* Top bar blu */
.top-bar {
    background: linear-gradient(135deg, #00338D 0%, #005EB8 100%);
    padding: 18px 32px;
    margin: -1rem -1rem 2rem -1rem;
    display: flex;
    align-items: center;
    gap: 16px;
}

.top-bar h1 {
    color: white !important;
    font-size: 22px !important;
    font-weight: 600 !important;
    margin: 0 !important;
    letter-spacing: 0.3px;
}

.top-bar .subtitle {
    color: rgba(255,255,255,0.75);
    font-size: 13px;
    margin: 0;
}

/* Card navigazione homepage */
.nav-card {
    background: white;
    border-radius: 4px;
    padding: 28px 24px;
    border-top: 4px solid #00338D;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    transition: box-shadow 0.2s;
    height: 100%;
}

.nav-card:hover {
    box-shadow: 0 6px 20px rgba(0,51,141,0.15);
}

.nav-card .card-icon {
    font-size: 32px;
    margin-bottom: 12px;
}

.nav-card h3 {
    color: #00338D !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    margin-bottom: 8px !important;
}

.nav-card p {
    color: #555 !important;
    font-size: 13px !important;
    line-height: 1.5 !important;
    margin: 0 !important;
}

.nav-card.green { border-top-color: #00875A; }
.nav-card.green h3 { color: #00875A !important; }

.nav-card.purple { border-top-color: #6554C0; }
.nav-card.purple h3 { color: #6554C0 !important; }

/* Login card */
.login-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 80vh;
}

.login-card {
    background: white;
    border-radius: 4px;
    padding: 48px 40px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.10);
    max-width: 420px;
    width: 100%;
    border-top: 5px solid #00338D;
}

.login-card h2 {
    color: #00338D !important;
    font-size: 22px !important;
    font-weight: 700 !important;
    margin-bottom: 4px !important;
}

.login-card .login-sub {
    color: #777;
    font-size: 13px;
    margin-bottom: 28px;
}

/* Bottoni */
.stButton > button {
    background-color: #00338D !important;
    color: white !important;
    border: none !important;
    border-radius: 3px !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    padding: 10px 24px !important;
    transition: background-color 0.2s !important;
}

.stButton > button:hover {
    background-color: #002A75 !important;
}

/* Input fields */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    border: 1px solid #D0D7E3 !important;
    border-radius: 3px !important;
    font-size: 14px !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #00338D !important;
    box-shadow: 0 0 0 2px rgba(0,51,141,0.12) !important;
}

/* Sezione header */
h1 { color: #00338D !important; font-weight: 700 !important; }
h2 { color: #00338D !important; font-weight: 600 !important; }
h3 { color: #1A1A2A !important; font-weight: 600 !important; }

/* Divider */
hr { border-color: #E8ECF4 !important; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #00338D !important;
}
section[data-testid="stSidebar"] * {
    color: white !important;
}
section[data-testid="stSidebar"] .stButton > button {
    background-color: rgba(255,255,255,0.15) !important;
    border: 1px solid rgba(255,255,255,0.3) !important;
    color: white !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background-color: rgba(255,255,255,0.25) !important;
}

/* Metriche */
[data-testid="stMetric"] {
    background: white;
    padding: 16px;
    border-radius: 4px;
    border-left: 4px solid #00338D;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}

/* Badge rischio */
.badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 3px;
    font-weight: 600;
    font-size: 12px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

/* Info/warning/success box */
.stAlert {
    border-radius: 3px !important;
}

/* Tabella */
.stDataFrame {
    border-radius: 4px !important;
    overflow: hidden !important;
}

/* Download button */
.stDownloadButton > button {
    background-color: white !important;
    color: #00338D !important;
    border: 2px solid #00338D !important;
}
.stDownloadButton > button:hover {
    background-color: #00338D !important;
    color: white !important;
}

/* Page link */
[data-testid="stPageLink"] a {
    display: block;
    background-color: #00338D;
    color: white !important;
    text-align: center;
    padding: 10px;
    border-radius: 3px;
    font-weight: 600;
    font-size: 14px;
    text-decoration: none !important;
    transition: background-color 0.2s;
}
[data-testid="stPageLink"] a:hover {
    background-color: #002A75;
}
</style>
"""


def inject_css() -> None:
    st.markdown(CSS, unsafe_allow_html=True)


def top_bar(title: str, subtitle: str = "") -> None:
    st.markdown(
        f'<div class="top-bar">'
        f'<div><p class="subtitle" style="margin:0;color:rgba(255,255,255,0.6);font-size:11px;letter-spacing:1px;text-transform:uppercase;">Meta Advisory</p>'
        f'<h1>{title}</h1>'
        f'{"<p class=subtitle>" + subtitle + "</p>" if subtitle else ""}'
        f'</div></div>',
        unsafe_allow_html=True,
    )
