"""Решения заданий lab07 с использованием NumPy."""

import numpy as np


def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    """Разбить плоский список на строки заданной ширины."""
    if width <= 0 or len(values) % width != 0:
        return []

    matrix = np.asarray(values, dtype=float).reshape(-1, width)
    return matrix.tolist()


def block(
    matrix: list[list[float]],
    rows: list[int],
    columns: list[int],
) -> list[list[float]]:
    """Выбрать строки и столбцы в указанном порядке."""
    array = np.asarray(matrix, dtype=float)

    if array.size == 0:
        return []

    return array[np.ix_(rows, columns)].tolist()


def column_means(matrix: list[list[float]]) -> list[float]:
    """Вернуть среднее значение каждого столбца."""
    array = np.asarray(matrix, dtype=float)

    if array.size == 0:
        return []

    means = np.mean(array, axis=0)
    return np.round(means, 6).tolist()


def column_range(matrix: list[list[float]], column: int) -> float:
    """Вернуть разницу между максимумом и минимумом в столбце."""
    array = np.asarray(matrix, dtype=float)

    if array.size == 0:
        return 0.0

    value_range = np.max(array[:, column]) - np.min(array[:, column])
    return round(float(value_range), 6)
