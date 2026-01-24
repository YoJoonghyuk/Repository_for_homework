import pandas as pd
from .base import Handler


class DataLoaderHandler(Handler):
    """Загрузчик с автоопределением разделителя и кодировки."""

    def handle(self, path: str) -> pd.DataFrame:
        try:
            # Автоопределение разделителя (sep=None)
            df = pd.read_csv(path, sep=None, engine='python', encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(path, sep=None, engine='python', encoding='cp1251')

        print(f"Файл загружен. Строк: {df.shape[0]}")
        return super().handle(df)
