import numpy as np


# Задание 1. Создание векторов и матриц
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("Задание 1")
print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)
print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)


# Задание 2. Индексы и срезы в векторе
print("\nЗадание 2")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])


# Задание 3. Строки и столбцы таблицы
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("\nЗадание 3")
print("shape:", temperatures.shape)
print("ndim:", temperatures.ndim)
print("size:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
central_temperatures = temperatures[0:2, 1:3]
print("Центральный фрагмент:\n", central_temperatures)
print("shape центрального фрагмента:", central_temperatures.shape)


# Задание 4. Прямоугольные срезы
matrix = np.arange(1, 26).reshape(5, 5)

print("\nЗадание 4")
print("Исходная матрица:\n", matrix)

matrix_parts = [
    ("Первые три строки", matrix[:3, :]),
    ("Последние две строки", matrix[-2:, :]),
    ("Первые два столбца", matrix[:, :2]),
    ("Строки 1–3 и столбцы 2–4", matrix[1:4, 2:5]),
    ("Правый нижний блок 2x2", matrix[-2:, -2:]),
]

for title, part in matrix_parts:
    print(title, ":\n", part)
    print("shape:", part.shape)


# Задание 5. Изменение массива с помощью срезов
print("\nЗадание 5")
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("Пример изменения vector:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("Пример изменения small_matrix:\n", small_matrix)

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print("changed_hours:", changed_hours)
print("Исходный hours:", hours)
# copy() нужен, чтобы изменения не затрагивали исходный массив hours.

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print("changed_matrix:\n", changed_matrix)
print("Исходная matrix:\n", matrix)
# copy() создаёт независимую копию. Без него срезы изменили бы matrix.


# Задание 6. Изменение формы
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("\nЗадание 6")
print("numbers:", numbers)
print("shape numbers:", numbers.shape)
print("table:\n", table)
print("shape table:", table.shape)
print("transposed:\n", transposed)
print("shape transposed:", transposed.shape)
# reshape(3, 4) работает, потому что 3 * 4 = 12 элементов.
# reshape(5, 3) вызовет ошибку, потому что 5 * 3 = 15, а элементов только 12.
