import streamlit as st
from supabase import create_client, Client


@st.cache_resource
def get_supabase() -> Client:
    """Restituisce il client Supabase (singleton per sessione)."""
    cfg = st.secrets["supabase"]
    return create_client(cfg["url"], cfg["service_key"])


def get_tenant() -> str:
    """Legge il nome del tenant dai secrets (es. 'flowpay', 'sarda_factoring')."""
    try:
        return st.secrets["supabase"]["tenant"]
    except Exception:
        return "default"


def salva_submission(tipo: int, nome_azienda: str, punteggio: int, livello: str, valore: int, dati: dict) -> str | None:
    """Salva una compilazione e restituisce l'ID generato."""
    try:
        res = (
            get_supabase()
            .table("submissions")
            .insert({
                "tipo_questionario": tipo,
                "nome_azienda": nome_azienda,
                "punteggio": punteggio,
                "livello_rischio": livello,
                "valore": valore,
                "dati": dati,
                "tenant": get_tenant(),
            })
            .execute()
        )
        return res.data[0]["id"] if res.data else None
    except Exception as e:
        st.warning(f"Salvataggio dati non riuscito: {e}")
        return None


def salva_documento(submission_id: str, nome_file: str, tipo_doc: str, file_bytes: bytes) -> None:
    """Carica un documento su Storage e registra il riferimento nel DB."""
    try:
        sb = get_supabase()
        tenant = get_tenant()
        path = f"{tenant}/{submission_id}/{tipo_doc}/{nome_file}"
        sb.storage.from_("documenti").upload(
            path,
            file_bytes,
            {"content-type": "application/octet-stream", "x-upsert": "true"},
        )
        sb.table("documenti").insert({
            "submission_id": submission_id,
            "nome_file": nome_file,
            "tipo_documento": tipo_doc,
            "storage_path": path,
            "tenant": tenant,
        }).execute()
    except Exception as e:
        st.warning(f"Salvataggio documento '{nome_file}' non riuscito: {e}")
