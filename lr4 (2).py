import numpy as np
import matplotlib.pyplot as plt
def read_matrix_from_file(filename):
    with open(filename, 'r') as f:
        return np.array([list(map(int, line.split())) for line in f])
def make_matrix_non_singular(matrix): #чтобы матрица не была выраждена
    n = matrix.shape[0]
    return matrix + np.eye(n) * 1e-10
def main():
    k = int(input("Введите k: "))
    n = int(input("Введите размер матрицы N: "))
    # Чтение матрицы A
    with open('matrix2.txt') as f:
        A = np.array([list(map(int, line.split()))[:n] for line in f][:n])
    print("Исходная матрица A:\n", A)
    # Создаем копию матрицы A для F
    F = A.copy()
    # Определяем подматрицы
    half = n // 2
    # Подматрица C (верхний правый блок)
    C = F[:half, half:] if n % 2 == 0 else F[:half, half + 1:]
    # Подсчет нулей в нечетных столбцах C
    zero_odd_cols = np.sum(C[:, 1::2] == 0)
    # Подсчет нулей в четных столбцах C
    zero_even_cols = np.sum(C[:, ::2] == 0)
    # Преобразование матрицы F
    if zero_odd_cols > zero_even_cols:
        # Меняем C и B симметрично
        if n % 2 == 0:
            B = F[half:, half:].copy()
            C = F[:half, half:].copy()
            F[:half, half:] = np.fliplr(B.T)  # Заменяем C на отраженную B
            F[half:, half:] = np.fliplr(C.T)  # Заменяем B на отраженную C
        else:
            B = F[half + 1:, half + 1:].copy()
            C = F[:half, half + 1:].copy()
            F[:half, half + 1:] = np.fliplr(B.T)
            F[half + 1:, half + 1:] = np.fliplr(C.T)
    else:
        # Меняем C и E несимметрично
        if n % 2 == 0:
            E = F[half:, :half].copy()
            C = F[:half, half:].copy()
            F[:half, half:] = E  # Заменяем C на E
            F[half:, :half] = C  # Заменяем E на C
        else:
            E = F[half + 1:, :half + 1].copy()
            C = F[:half, half + 1:].copy()
            F[:half, half + 1:] = E
            F[half + 1:, :half + 1] = C
    # Гарантируем, что F не вырождена
    F = make_matrix_non_singular(F)
    print("\nПреобразованная матрица F:\n", F)
    # Вычисляем условия для выбора выражения
    det_A = np.linalg.det(A)
    sum_diag_F = np.trace(F)
    if det_A > sum_diag_F:
        # Вычисляем A*AT - K*FT
        AT = A.T
        FT = F.T
        result = A @ AT - k * FT
    else:
        # Вычисляем (AT + G - F-1)*K
        AT = A.T
        G = np.tril(A)  # Нижняя треугольная матрица из A
        F_inv = np.linalg.inv(F)  # Теперь гарантированно не вырождена
        result = (AT + G - F_inv) * k
    print("\nРезультат вычислений:\n", result)
    # Визуализация
    plt.figure(figsize=(15, 5))
    # 1. Тепловая карта матрицы F
    plt.subplot(131)
    plt.imshow(F, cmap='magma', interpolation='nearest')
    plt.colorbar()
    plt.title("Тепловая карта F")
    # 2. График суммы по строкам
    plt.subplot(132)
    plt.plot(F.sum(axis=1), 'o-', color='blue')
    plt.title("Сумма по строкам")
    plt.grid(True)
    # 3. Столбчатая диаграмма
    plt.subplot(133)
    plt.bar(range(F.shape[1]), F.sum(axis=0), color='green', alpha=0.7)
    plt.title("Сумма по столбцам")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    main()