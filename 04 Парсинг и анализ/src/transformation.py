import pandas as pd
import numpy as np
from .base import Handler
from utils.parsers import extract_age, extract_experience, extract_salary
from utils.helpers import find_column_name

class FeatureExtractionHandler(Handler):
    """Извлечение X (признаки) и y (таргет)."""
    def handle(self, df: pd.DataFrame) -> dict:
        # Умный поиск нужных колонок
        col_personal = find_column_name(df, 'Пол, возраст')
        col_exp = find_column_name(df, 'Опыт')
        col_salary = find_column_name(df, 'ЗП')

        # Применяем парсеры
        age = df[col_personal].apply(extract_age)
        is_male = df[col_personal].apply(lambda x: 1 if 'Мужчина' in str(x) else 0)
        experience = df[col_exp].apply(extract_experience)
        salary = df[col_salary].apply(extract_salary)

        # Формируем матрицы (float32 для экономии памяти и совместимости с ML)
        x_data = np.column_stack((is_male, age, experience)).astype(np.float32)
        y_data = salary.values.astype(np.float32)

        return super().handle({'x': x_data, 'y': y_data})
