import pandas as pd
from src.services.sheets_service import append_rows

ABA_ATENDIMENTOS_RAW = "Atendimentos RAW"

def append_atendimentos_rows(rows: list[list]):
    append_rows(ABA_ATENDIMENTOS_RAW, rows)
