import random
import copy

def reader(filename):
    with open(filename, 'r') as file:
        return [list(map(int, line.split())) for line in file]

k, n = int(input("Введите число k: ")), int(input("Введите число n: "))
KON, UMN, Fk, A, A_B, G, x = [], [], [], [], [], 0, n

# Инициализация матриц
for i in range(n):
    A.append([0] * n)
    A_B.append([0] * n)
    Fk.append([0] * n)
    UMN.append([0] * n)
    KON.append([0] * n)

# Чтение матрицы A из файла
A = reader('matrix.txt')
print("Матрица A: ")
for i in range(n):
    print(f"{A[i]}")

# Копируем матрицу A в F
F = copy.deepcopy(A)

# Подсчет четных чисел в нечетных столбцах области 2 и нулевых элементов в четных строках области 3
count_even_odd_col2 = 0
count_zero_even_row3 = 0

# Область 2: строки 0-2, нечетные столбцы (1, 3)
for i in range(3):
    for j in [1, 3]:
        if i < len(F) and j < len(F[i]) and F[i][j] % 2 == 0:
            count_even_odd_col2 += 1

# Область 3: строки 3-6, четные столбцы (0, 2)
for i in range(3, 7):
    if i < len(F):
        for j in [0, 2]:
            if j < len(F[i]) and F[i][j] == 0:
                count_zero_even_row3 += 1

# Проверяем условие
if count_even_odd_col2 > count_zero_even_row3:
    # Меняем местами области 1 и 3 симметрично
    for i in range(3):  # строки 0-2
        for j in range(3):  # столбцы 0-2
            if i + 3 < len(F):
                F[i][j], F[i + 3][j] = F[i + 3][j], F[i][j]
else:
    # Меняем местами области 3 и 4 несимметрично
    for i in range(3):  # строки 3-5
        for j in range(3):  # столбцы 3-5
            if i < len(F) and j + 3 < len(F[i]):
                F[i + 3][j + 3] = F[i][j]

print("Матрица F: ")
for i in range(n):
    print(f"{F[i]}")

# Вычисление матрицы A_B, Fk, UMN и KON
AT = [[0 for j in range(len(A))] for i in range(len(A[0]))]
for i in range(len(AT)):
    for j in range(len(AT)):
        AT[j][i] = A[i][j]

for i in range(len(AT)):
    for j in range(len(AT)):
        A_B[i][j] = (A[i][j] + F[i][j])
        Fk[i][j] = F[i][j] * k
        for m in range(len(AT)):
            UMN[i][j] += A_B[i][m] * AT[m][j]
        KON[i][j] = UMN[i][j] - Fk[i][j]

print("Матрица, равная сумме матриц F и A:")
for i in range(n):
    print(f"{A_B[i]}")

print("Матрица (F + A) * AT:")
for i in range(n):
    print(f"{UMN[i]}")

print(f"Матрица, равная произведению матрицы F и числа {k}:")
for i in range(n):
    print(f"{Fk[i]}")

print("Результат:")
for i in range(n):
    print(f"{KON[i]}")
    print(f"{KON[i]}")