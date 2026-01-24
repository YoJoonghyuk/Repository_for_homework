import pandas as pd
import numpy as np
from .base import Handler
from utils.parsers import extract_age, extract_experience, extract_salary
from utils.helpers import find_column_name

class FeatureExtractionHandler(Handler):
    """
    Обработчик, который извлекает и трансформирует сырые данные из DataFrame
    в числовые признаки (X) и целевую переменную (y).
    Включает парсинг пола/возраста, опыта работы и зарплаты.
    """
    def handle(self, df: pd.DataFrame) -> dict:
        """
        Выполняет извлечение признаков и формирование целевой переменной.
        Использует вспомогательные функции для парсинга

        Args:
            df: pandas.DataFrame, содержащий исходные данные резюме.

        Returns:
            Словарь, содержащий:
            'x': numpy.ndarray - матрица признаков (пол, возраст, опыт).
            'y': numpy.ndarray - вектор целевой переменной (зарплата).
            Все массивы приведены к типу float32.

        Raises:
            KeyError: Если одна из необходимых колонок не найдена.
        """
        col_personal = find_column_name(df, 'Пол, возраст')
        col_exp = find_column_name(df, 'Опыт')
        col_salary = find_column_name(df, 'ЗП')

        age = df[col_personal].apply(extract_age)
        is_male = df[col_personal].apply(lambda x: 1 if 'Мужчина' in str(x) else 0)
        experience = df[col_exp].apply(extract_experience)
        salary = df[col_salary].apply(extract_salary)

        # Формируем матрицу признаков (X) и вектор целевой переменной (y)
        # Приводим к float32 для совместимости с ML-фреймворками и экономии памяти
        x_data = np.column_stack((is_male, age, experience)).astype(np.float32)
        y_data = salary.values.astype(np.float32)

        return super().handle({'x': x_data, 'y': y_data})