import os
import numpy as np
from .base import Handler

class NpySaveHandler(Handler):
    """
    Обработчик, отвечающий за сохранение результирующих массивов NumPy
    (матрицы признаков X и вектора целевой переменной y) в файлы .npy.
    """
    def __init__(self, target_path: str):
        """
        Инициализирует NpySaveHandler.
        Определяет директорию для сохранения файлов на основе пути к исходному CSV.

        Args:
            target_path: Путь к исходному CSV-файлу, используемый для определения
                         места сохранения выходных файлов.
        """
        self.directory = os.path.dirname(os.path.abspath(target_path))

    def handle(self, data: dict) -> str:
        """
        Сохраняет матрицу признаков 'x_data.npy' и вектор целевой переменной 'y_data.npy'.

        Args:
            data: Словарь, содержащий два ключа:
                  'x': numpy.ndarray - матрица признаков.
                  'y': numpy.ndarray - вектор целевой переменной.

        Returns:
            Строковое сообщение об успешном сохранении и пути к файлам.
        """
        x_path = os.path.join(self.directory, 'x_data.npy')
        y_path = os.path.join(self.directory, 'y_data.npy')

        np.save(x_path, data['x'])
        np.save(y_path, data['y'])

        return f"Успех! Файлы x_data.npy и y_data.npy созданы в: {self.directory}"