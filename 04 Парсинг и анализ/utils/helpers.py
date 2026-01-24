import pandas as pd

def find_column_name(df: pd.DataFrame, keyword: str) -> str:
    """Умный поиск колонки по ключевому слову."""
    for col in df.columns:
        if keyword.lower() in str(col).lower():
            return col
    raise KeyError(f"Колонка с ключевым словом '{keyword}' не найдена.")
