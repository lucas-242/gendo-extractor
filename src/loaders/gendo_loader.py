import pandas as pd
from src.services.sheets_service import read_sheet


def load_gendo_csv(csv_path: str) -> pd.DataFrame:
    """Loads and processes Gendo CSV."""
    df = pd.read_csv(
        csv_path,
        sep=",",
        encoding="utf-8"
    )

    df["Total"] = pd.to_numeric(df["Total"], errors="coerce")
    df = df[df["Total"].notna()]

    df["ID externo"] = (
        df["Cód. Comanda"].astype(str)
        + "|"
        + df["Serviço"].astype(str)
        + "|"
        + df["Total"].astype(str)
    )

    return df


def filter_new_atendimentos(df: pd.DataFrame) -> pd.DataFrame:
    """Filters only new appointments that do not exist in the sheet."""
    existing = read_sheet("Atendimentos RAW")
    
    if not existing.empty and "ID externo" in existing.columns:
        existing_ids = set(existing["ID externo"].astype(str))
        df = df[~df["ID externo"].isin(existing_ids)]
    
    return df


def format_for_export(df: pd.DataFrame) -> list[list]:
    """Formats DataFrame rows for export."""
    df = df.fillna("")

    df["Forma Pagto"] = df["Forma Pagto"].replace({
        "PIX (Externo)": "Pix",
        "*Credito Pacote": "Crédito Pacote"
    })
    
    rows = []
    for _, row in df.iterrows():
        rows.append([
            str(row["Data"]),
            str(row["Colaborador"]),
            str(row["Serviço"]),
            str(row["Qts"]),
            str(row["Categoria"]),
            float(row["Total"]),
            str(row["Forma Pagto"]),
            "Gendo",
            str(row["ID externo"]),
        ])
    
    return rows
