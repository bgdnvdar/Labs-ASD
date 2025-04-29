import itertools


def generate_optimized_matrix(matrix):
    n = len(matrix)
    diagonal_pairs = []

    # Собираем пары элементов с главной и побочной диагоналей
    for i in range(n):
        main_diag = matrix[i][i]
        anti_diag = matrix[i][n - 1 - i]
        diagonal_pairs.append([(main_diag, anti_diag), (anti_diag, main_diag)])

    # Генерируем все возможные комбинации
    variants = itertools.product(*diagonal_pairs)

    best_matrix = None
    min_roughness = float('inf')

    for variant in variants:
        # Проверяем ограничение на четность суммы главной диагонали
        main_diag_sum = sum(variant[i][0] for i in range(n))
        if main_diag_sum % 2 != 0:
            continue

        # Создаем новую матрицу
        new_matrix = [row.copy() for row in matrix]
        for i in range(n):
            new_matrix[i][i] = variant[i][0]
            new_matrix[i][n - 1 - i] = variant[i][1]

        # Вычисляем целевую функцию (сумму абсолютных разностей в строках)
        current_roughness = 0
        for row in new_matrix:
            row_roughness = sum(abs(row[j] - row[j + 1]) for j in range(n - 1))
            current_roughness += row_roughness

        # Обновляем лучшее решение
        if current_roughness < min_roughness:
            min_roughness = current_roughness
            best_matrix = new_matrix

    return best_matrix, min_roughness


# Пример использования
matrix = [
    [4, 3, 7],
    [1, 5, 2],
    [6, 8, 9]
]

optimized_matrix, roughness = generate_optimized_matrix(matrix)

print("Оптимальная матрица:")
for row in optimized_matrix:
    print(row)
print(f"Минимальная 'шероховатость': {roughness}")