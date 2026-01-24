import argparse
import sys
import os

from src.loaders import DataLoaderHandler
from src.transformation import FeatureExtractionHandler
from src.output import NpySaveHandler

def run_pipeline():
    """
    Функция запуска пайплайна обработки данных.
    Парсит аргументы командной строки, собирает и конфигурирует цепочку
    обработчиков (Chain of Responsibility), после чего запускает процесс
    обработки данных.
    """
    parser = argparse.ArgumentParser(description="HH Resume Data Processor")
    parser.add_argument("path", help="Путь к исходному CSV файлу резюме HeadHunter.")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Ошибка: Файл '{args.path}' не найден. Пожалуйста, укажите корректный путь.")
        sys.exit(1)

    loader = DataLoaderHandler()
    transformer = FeatureExtractionHandler()
    saver = NpySaveHandler(args.path)

    loader.set_next(transformer).set_next(saver)

    try:
        result_message = loader.handle(args.path)
        print(result_message)
    except Exception as e:
        print(f"Произошла критическая ошибка в пайплайне: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_pipeline()