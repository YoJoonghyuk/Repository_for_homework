import pandas as pd
from .base import Handler

class DataLoaderHandler(Handler):
    """
    Обработчик, отвечающий за загрузку данных из CSV-файла.
    Автоматически определяет разделитель (sep=None) и пытается подобрать
    кодировку (utf-8, cp1251) для устойчивости к различным форматам файлов HH.
    """
    def handle(self, path: str) -> pd.DataFrame:
        """
        Загружает данные из CSV-файла по указанному пути.
        Пытается загрузить файл с кодировкой 'utf-8', если не удается,
        переключается на 'cp1251'. Использует engine='python' и sep=None
        для автоматического определения разделителя.

        Args:
            path: Абсолютный или относительный путь к CSV-файлу.

        Returns:
            Загруженный pandas.DataFrame.

        Raises:
            Exception: В случае других ошибок при чтении файла.
        """
        try:
            df = pd.read_csv(path, sep=None, engine='python', encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(path, sep=None, engine='python', encoding='cp1251')

        print(f"Файл загружен. Строк: {df.shape[0]}")
        return super().handle(df)