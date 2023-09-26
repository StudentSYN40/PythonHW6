# Ввод целых чисел A и B
a = int(input("Введите целое число A: "))
b = int(input("Введите целое число B (A ≤ B): "))

# Вывод четных чисел на заданном отрезке
for num in range(a, b + 1):
    if num % 2 == 0:
        print(num, end=' ')