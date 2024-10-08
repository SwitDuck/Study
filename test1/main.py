'''
X =99
def f1():
    X = 88
    def f2():
        print(X)
    f2()
f1()'''

#Задачи

#Задача 1
'''
Анализ и обработка данных. Дан список кортежей, где каждый кортеж представляет собой данные о сотруднике:
его имя, возраст и должность.
1)Создай словарь, где ключами будут должности, а значениями списки имен сотрудников, которые занимают эти должности.
2)Напиши функцию, которая принимает этот словарь и должность, 
а затем возвращает средний возраст сотрудников на этой должности.
3)С помощью генераторов создай список сотрудников старше 25 лет, сохранив все данные о них.
4)Используя циклы, напиши функцию, которая найдет самого старшего сотрудника в каждой должности.
'''
#функция списка сотрудников старше 25
'''
def aging(*args):
    spisok = []
    for i in args:
        for name,age,job in i:
            if age >= 25:
                spisok.append(f"{name} - {job}({age})")
    return spisok
def func1(*args):
    totalage = 0
    for i in args:
        for name,age,job in i:
            totalage += age
    mod = age / len(args)
    print(mod)
#def diction():

employees = [
    ("Андрей", 30, "Инженер"),
    ("Мария", 22, "Аналитик"),
    ("Иван", 35, "Менеджер"),
    ("Елена", 28, "Инженер"),
    ("Павел", 45, "Директор"),
    ("Анна", 23, "Аналитик")
]
func1(employees)
for i in aging(employees):
    print(i)
'''

#Функции
'''1. Основы функции
Напиши функцию multiply(a, b), которая принимает два числа и возвращает их произведение. 
Попробуй использовать эту функцию с разными аргументами и напечатай результаты.
2. Функция с аргументами по умолчанию
Реализуй функцию greet(name, greeting='Hello'), которая принимает имя и приветствие, и возвращает строку вида:
"Приветствие, имя!". Если приветствие не передано, используй 'Hello' по умолчанию.
3. Функция с произвольным числом аргументов
Напиши функцию average(*args), которая принимает любое количество чисел и возвращает их среднее значение. 
Обрабатывай случай, когда аргументы не передаются.

def multiply(a, b):
    return a*b
def greet(name='default_name', greeting='hello'):
    greeting = 'hello'
    print(f'{greeting}, {name}!')
greet('Sieg', 'Heil')
def average(*args):
    if len(args) == 0:
        #raise TypeError("Функция должна получить хотя бы один аргумент")
        return None
    else:
        return sum(args)/len(args)
'''

#Nonlocal
'''
1. Использование nonlocal для изменения переменной в замыкании
Напиши функцию outer(), которая содержит переменную counter. Внутри outer напиши вложенную функцию inner(), 
которая увеличивает counter на 1 каждый раз при вызове. outer должна возвращать функцию inner. 
Продемонстрируй, как можно использовать эту функцию.
2. Счётчик с помощью nonlocal
Реализуй функцию create_counter(), которая возвращает две функции: increment() и get_count(). 
increment() увеличивает внутренний счётчик на 1, а get_count() возвращает текущее значение счётчика. 
Используй nonlocal для доступа к счётчику внутри increment().
3. Функция с изменяемым состоянием
Напиши функцию make_multiplier(x) которая возвращает функцию multiplier(y), которая умножает y на x. 
Используй nonlocal для хранения значения x внутри функции multiplier.
'''
'''
def outer():
    counter = 1
    def inner():
        nonlocal counter
        counter+=1
        return counter
    return inner
def create_couner():
    counter = 1
    def increment():
        nonlocal counter; counter+=1
        return counter
    def get_count():
        return counter
    return get_count, increment
def make_multiplier(x):
    def multiplier(y):
        return x * y
    return multiplier
multiply = make_multiplier(5)
print(multiply(6))
'''
#Lambda
'''
1. Сортировка с помощью lambda
Напиши функцию sort_by_length(strings), которая принимает список строк и возвращает его отсортированным по длине строк 
с использованием функции lambda.
2. Использование lambda в функции map
Реализуй программу, которая принимает список чисел и возвращает список их квадратов, используя функцию map и lambda.
3. Фильтрация списка с помощью lambda
Напиши функцию filter_even(numbers), которая принимает список чисел и возвращает новый список, 
содержащий только четные числа. Используй lambda и filter для решения задачи.
'''

#Global
'''
1. Изменение глобальной переменной
Напиши функцию update_global_var() которая изменяет значение глобальной переменной global_var на 'Updated'. 
Покажи, как использовать global для изменения глобальной переменной.
2. Глобальная и локальная переменные
Реализуй функцию set_values() которая устанавливает значение глобальной переменной value в 'Global Value' 
и локальной переменной value в 'Local Value'. Напечатай оба значения внутри функции и вне её.
3. Использование глобальных переменных в функциях
Напиши функцию increase_counter() которая увеличивает глобальную переменную counter на 1 при каждом вызове. 
Покажи, как обновляется значение counter при многократных вызовах функции.
'''
'''
global_var = ''
def update_global_var():
    global global_var; global_var = 'updated'
update_global_var()
'''

#Reduce
'''
1. Сумма чисел с использованием reduce
Реализуй функцию sum_list(numbers) которая принимает список чисел и возвращает их сумму, используя функцию reduce из модуля functools.
2. Произведение чисел с использованием reduce
Напиши функцию product_list(numbers) которая принимает список чисел и возвращает их произведение, используя reduce и функцию lambda.
3. Нахождение максимального числа с использованием reduce
Реализуй функцию max_list(numbers) которая находит и возвращает максимальное число в списке, используя reduce и функцию lambda.
'''
'''
import functools as f
def sum_list(numbers):
    return f.reduce(lambda x,y:x+y, numbers)
def product_list(numbers):
    return f.reduce(lambda x,y: x*y, numbers)
def max_list(numbers):
    return f.reduce(lambda x,y: x if x>y else y, numbers)
#Решение chatgpt
import operator
def max_list(numbers):
    return f.reduce(max, numbers)
def product_list(numbers):
    return f.reduce(operator.mul, numbers)
def sum_list(numbers):
    return f.reduce(operator.add, numbers)
'''

#Filter
'''
1. Фильтрация строк по длине
Напиши функцию filter_long_words(words, n) которая принимает список строк и число n, и возвращает список строк 
длиной больше n, используя filter и lambda.
2. Фильтрация четных чисел
Реализуй функцию filter_even_numbers(numbers) которая принимает список чисел и возвращает только четные числа, 
используя filter и функцию lambda.
3. Фильтрация положительных чисел
Напиши функцию filter_positive(numbers) которая возвращает список только положительных чисел из переданного списка,
 используя filter и lambda.
'''
'''
def filter_long_words(words, n):
    return list(filter(lambda x : len(x)>n, words))
def filter_even_numbers(numbers):
    return list(filter(lambda x : x%2==0, numbers))
def filter_positive(numbers):
    return list(filter(lambda x: x>0, numbers))'''

#Map
'''
1. Преобразование строк в верхний регистр
Реализуй функцию to_uppercase(words) которая принимает список строк и возвращает список, где каждая строка 
преобразована в верхний регистр, используя map и lambda.
2. Преобразование чисел в их квадратные корни
Напиши функцию square_roots(numbers) которая принимает список чисел и возвращает список их квадратных корней, 
используя map и lambda.
3. Форматирование списка чисел
Реализуй функцию format_numbers(numbers) которая принимает список чисел и возвращает список строк с числовыми значениями,
 отформатированными до двух знаков после запятой, используя map и lambda.
'''
'''def to_uppercase(words):
    return list(map(lambda x: x.upper(), words))
def square_roots(numbers):
    return list(map(lambda x: x**(1/2), numbers))
def format_numbers(numbers):
    return list(map(lambda x: '{:.2f}'.format(x), numbers))'''

#Yield
'''
1. Генератор чисел Фибоначчи
Реализуй генератор fibonacci() который генерирует числа Фибоначчи до бесконечности. 
Используй yield для возвращения каждого следующего числа.
2. Генератор четных чисел
Напиши генератор even_numbers(n) который возвращает первые n четных чисел. Используй yield для генерации чисел.
3. Генератор квадратов чисел
Реализуй генератор squares(start, end) который возвращает квадраты чисел от start до end, 
используя yield для генерации каждого квадрата.
'''
'''
def fibonacci():
    a, b = 0, 1  # Первые два числа Фибоначчи
    while True:
        yield a
        a, b = b, a + b
x = fibonacci()
for _ in range(10):
    print(next(x))
def even_numbers(n):
    for i in range(1,n):
        if i %2 ==0:
            yield i
def squares(start, end):
    for i in range(start, end):
        yield i**2
'''