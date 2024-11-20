"""
Задание: Декораторы в Python

Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
Пример:
result = sum_three(2, 3, 6)
print(result)

"""

def is_prime(func):
    def wrapper(*numbers):
        result_func = func(*numbers)
        is_prime = True
        for i in range(2,result_func):
            if result_func % i == 0:
                is_prime = False
        if  is_prime:
            print('простое')
        else:
            print('составное')
        return result_func
    return wrapper

@ is_prime
def sum_three(*numbers):
    return sum(numbers)

result = sum_three(2,3,6)
print(result)