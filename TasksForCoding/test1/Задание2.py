'''Создайте программу, которая считывает данные из CSV-файла, обрабатывает их 
и выводит статистику по каждому столбцу. Например, если файл содержит оценки студентов, программа должна:
Рассчитать средний балл для каждого студента.
Найти минимальный и максимальный балл по каждому предмету.
Вывести имена студентов с наибольшими и наименьшими средними баллами.
Подсказки:
Используйте модуль csv для работы с CSV-файлами.
Реализуйте функции для вычисления среднего значения, максимума и минимума.'''
import csv
def csv_write(file):
    with open(file, 'w', newline='\n') as File:
        csv.writer(File).writerows([['alex', 'math', '4.5'], ['danil', 'math', '3'], ['david', 'math', '4'], ['Egor','math','4.6']])

csv_write('zad1.csv')

rows = 0; medium = 0; maximum = 0; minimum = 0; columns = []
with open('zad1.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        columns.append(row[2])
minimum = min(columns)
maximum = max(columns)
#medium = sum(columns)/len(columns)
print(minimum,maximum)

#Правильное решение chatgpt
import csv

# Функция для записи данных в CSV
def csv_write(file):
    data = [['alex', 'math', '4.5'], 
            ['danil', 'math', '3'], 
            ['david', 'math', '4'], 
            ['Egor', 'math', '4.6']]
    
    with open(file, 'w', newline='', encoding='utf-8') as File:
        writer = csv.writer(File)
        writer.writerow(['Name', 'Subject', 'Grade'])  # Заголовки столбцов
        writer.writerows(data)

csv_write('zad1.csv')

# Переменные для хранения данных
students = []

# Чтение файла и обработка данных
with open('zad1.csv', newline='', encoding='utf-8') as File:  
    reader = csv.reader(File)
    next(reader)  # Пропуск заголовков
    for row in reader:
        name = row[0]
        subject = row[1]
        grade = float(row[2])
        students.append({'name': name, 'subject': subject, 'grade': grade})

# Поиск минимальной и максимальной оценки
min_student = min(students, key=lambda x: x['grade'])
max_student = max(students, key=lambda x: x['grade'])

# Расчет средней оценки
average_grade = sum(student['grade'] for student in students) / len(students)

# Вывод результатов
print(f"Студент с минимальной оценкой: {min_student['name']} - {min_student['grade']}")
print(f"Студент с максимальной оценкой: {max_student['name']} - {max_student['grade']}")
print(f"Средняя оценка: {average_grade:.2f}")

    