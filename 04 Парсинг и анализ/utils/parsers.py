import re

def extract_age(text: str) -> int:
    """Извлекает возраст в годах."""
    if not isinstance(text, str): return 30
    match = re.search(r'(\d+)\s+(?:год|года|лет)', text)
    return int(match.group(1)) if match else 30

def extract_experience(text: str) -> int:
    s = str(text)
    if s == 'nan' or 'Не указано' in s: return 0

    # Ищем все вхождения чисел и слов год/лет/месяц
    years = re.search(r'(\d+)\s+(?:год|года|лет)', s)
    months = re.search(r'(\d+)\s+(?:месяц|месяца|месяцев)', s)

    y = int(years.group(1)) if years else 0
    m = int(months.group(1)) if months else 0

    # Защита от парсинга текущего года (например, 2019, 2024)
    if y > 100:  # Если лет больше 100, скорее всего это год даты
        y = 0

    return y * 12 + m

def extract_salary(text: str) -> float:
    """Парсит ЗП и приводит к числу."""
    if not isinstance(text, str): return 0.0
    num = re.sub(r'[^\d]', '', text)
    return float(num) if num else 0.0
