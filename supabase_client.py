import streamlit as st
from supabase import create_client, Client


@st.cache_resource
def get_supabase() -> Client:
    """Restituisce il client Supabase (singleton per sessione)."""
    cfg = st.secrets["supabase"]
    return create_client(cfg["url"], cfg["service_key"])


def get_tenant() -> str:
    """Legge il nome del tenant dai secrets."""
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
                "nome_servizio_ict": nome_azienda,
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


def carica_submissions(tipo: int) -> list[dict]:
    """Carica tutte le submission di un tipo per il tenant corrente."""
    try:
        res = (
            get_supabase()
            .table("submissions")
            .select("id, nome_servizio_ict, livello_rischio, valore, created_at, dati")
            .eq("tipo_questionario", tipo)
            .eq("tenant", get_tenant())
            .order("created_at", desc=True)
            .execute()
        )
        return res.data or []
    except Exception as e:
        st.warning(f"Caricamento dati non riuscito: {e}")
        return []


def carica_registro() -> list[dict]:
    """Carica tutte le voci del registro rischi per il tenant corrente."""
    try:
        res = (
            get_supabase()
            .table("registro_rischi")
            .select("*")
            .eq("tenant", get_tenant())
            .order("created_at", desc=True)
            .execute()
        )
        return res.data or []
    except Exception as e:
        st.warning(f"Caricamento registro non riuscito: {e}")
        return []


def salva_registro(
    servizio_tic: str,
    fornitore_tic: str,
    funzione_essenziale: bool,
    submission_q1_id: str,
    submission_q2_id: str,
    rischio_inerente: str,
    misure_sicurezza: str,
    rischio_residuo: str,
) -> bool:
    """Salva una voce nel registro rischi."""
    try:
        get_supabase().table("registro_rischi").insert({
            "tenant": get_tenant(),
            "servizio_tic": servizio_tic,
            "fornitore_tic": fornitore_tic,
            "funzione_essenziale": funzione_essenziale,
            "submission_q1_id": submission_q1_id,
            "submission_q2_id": submission_q2_id,
            "rischio_inerente": rischio_inerente,
            "misure_sicurezza": misure_sicurezza,
            "rischio_residuo": rischio_residuo,
        }).execute()
        return True
    except Exception as e:
        st.warning(f"Salvataggio registro non riuscito: {e}")
        return False


def elimina_registro(row_id: str) -> bool:
    """Elimina una voce dal registro rischi."""
    try:
        get_supabase().table("registro_rischi").delete().eq("id", row_id).execute()
        return True
    except Exception as e:
        st.warning(f"Eliminazione non riuscita: {e}")
        return False
