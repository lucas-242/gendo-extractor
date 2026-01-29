from src.loaders.gendo_loader import load_gendo_csv, filter_new_atendimentos, format_for_export
from src.exporters.atendimentos_raw_exporter import append_atendimentos_rows
from src.config import GENDO_CSV_PATH

def main():
    df = load_gendo_csv(GENDO_CSV_PATH)
    
    new_df = filter_new_atendimentos(df)
    
    if new_df.empty:
        print("✅ Nenhum atendimento novo para importar")
        return
    
    rows = format_for_export(new_df)
    
    append_atendimentos_rows(rows)
    print(f"✅ {len(rows)} atendimentos adicionados com sucesso")

if __name__ == "__main__":
    main()