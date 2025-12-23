import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from src.config import GOOGLE_CREDENTIALS_FILE, SPREADSHEET_NAME

SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

def get_client():
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        GOOGLE_CREDENTIALS_FILE, SCOPE
    )
    return gspread.authorize(creds)

def get_worksheet(aba_nome: str):
    """Retorna worksheet específica."""
    client = get_client()
    sheet = client.open(SPREADSHEET_NAME)
    return sheet.worksheet(aba_nome)

def read_sheet(aba_nome: str) -> pd.DataFrame:
    worksheet = get_worksheet(aba_nome)
    values = worksheet.get_all_values()

    if len(values) < 2:
        return pd.DataFrame()

    headers = values[0]
    rows = values[1:]

    return pd.DataFrame(rows, columns=headers)

def append_rows(aba_nome: str, rows: list[list]):
    if not rows:
        return
    
    worksheet = get_worksheet(aba_nome)
    worksheet.append_rows(rows, value_input_option="USER_ENTERED")
