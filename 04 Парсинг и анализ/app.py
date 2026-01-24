import argparse
import sys
import os
from src.loaders import DataLoaderHandler
from src.transformation import FeatureExtractionHandler
from src.output import NpySaveHandler

def run_pipeline():
    parser = argparse.ArgumentParser(description="HH Resume Data Processor")
    parser.add_argument("path", help="Путь к исходному CSV файлу")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Ошибка: Файл {args.path} не найден.")
        sys.exit(1)

    # Собираем цепь (Chain of Responsibility)
    loader = DataLoaderHandler()
    transformer = FeatureExtractionHandler()
    saver = NpySaveHandler(args.path)

    loader.set_next(transformer).set_next(saver)

    try:
        result_message = loader.handle(args.path)
        print(result_message)
    except Exception as e:
        print(f"Произошла ошибка при обработке: {e}")

if __name__ == "__main__":
    run_pipeline()
