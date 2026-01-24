import os
import numpy as np
from .base import Handler


class NpySaveHandler(Handler):
    """Сохранение результатов."""

    def __init__(self, target_path: str):
        self.directory = os.path.dirname(os.path.abspath(target_path))

    def handle(self, data: dict) -> str:
        x_path = os.path.join(self.directory, 'x_data.npy')
        y_path = os.path.join(self.directory, 'y_data.npy')

        np.save(x_path, data['x'])
        np.save(y_path, data['y'])

        return f"Успех! Файлы x_data.npy и y_data.npy созданы в: {self.directory}"
