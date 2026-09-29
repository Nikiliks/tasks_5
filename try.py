# task_1:
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 / num2
    print(f"Результат: {num1} / {num2} = {result}")

except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")

except ValueError:
    print("Некорректное значение переменных")

finally:
    print("Операция завершена.")

# task_2:

import math

class NegativeNumberError(Exception):
    """Возникает при попытке вычислить корень из отрицательного числа."""
    pass

def my_sqrt(number):
    if number < 0:
        raise NegativeNumberError(
            f"Невозможно вычислить квадратный корень из отрицательного числа: {number}"
        )
    return math.sqrt(number)

try:
    number = float(input("Введите число: "))
    result = my_sqrt(number)
    print(f"Квадратный корень из {number} = {result}")

except NegativeNumberError as e:
    print(f"Ошибка: {e}")

finally:
    print("Операция завершена.")

# task_3:
filename = input("Введите имя файла для чтения: ")

try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("\n--- Содержимое файла ---")
        print(content)

except FileNotFoundError:
    print(f"Ошибка: Файл '{filename}' не найден.")

except PermissionError:
    print(f"Ошибка: Недостаточно прав для чтения файла '{filename}'.")

except IsADirectoryError:
    print(f"Ошибка: '{filename}' является папкой, а не файлом.")

except UnicodeDecodeError:
    print(f"Ошибка: не удалось декодировать файл '{filename}' (возможно, это бинарный файл).")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    print("Операция завершена.")