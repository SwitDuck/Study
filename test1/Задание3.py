'''Задача 3: Лог-анализатор с использованием регулярных выражений
Создайте программу для анализа логов веб-сервера. Программа должна:

Считывать файл логов и извлекать все IP-адреса.
Определить, сколько раз каждый IP-адрес обращался к серверу.
Найти все уникальные URL-адреса, к которым были обращения.
Найти все строки, где статус ответа сервера — ошибка (4xx и 5xx коды).
Подсказки:

Лог-файл веб-сервера обычно содержит строки формата: IP-адрес - - [дата] "HTTP-метод URL HTTP/1.x" код-статуса размер.
Используйте регулярные выражения для извлечения IP-адресов, URL-адресов и кодов статуса.'''
ip_list = []
text_list = []
url_list = []
import re as r
with open(r'log1.log', 'r') as File:
    for line in File:
        ip_list.append(r.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line))
        code_pattern = r'HTTP/\d\.\d"\s(4\d{2}|5\d{2})\s'
        if r.search(code_pattern, line) != None:
            text_list.append(line)
        url_pattern = r'/[a-zA-Z0-9._-]+\s+"?HTTP'
        url_list.append(r.findall(url_pattern, line))
print(text_list)
print(' '.join(item[0] for item in ip_list))
print(' '.join(item[0] for item in url_list))


#Решение chatgpt
import re
from collections import Counter
def analyze_log(file_path):
    ip_counter = Counter()
    url_set = set()
    error_lines = []
    ip_pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    url_pattern = re.compile(r'GET\s+([^\s]+)')
    error_code_pattern = re.compile(r'HTTP/\d\.\d"\s(4\d{2}|5\d{2})\s')
    
    with open(file_path, 'r') as file:
        for line in file:
            ip_matches = ip_pattern.findall(line)
            if ip_matches:
                ip_counter.update(ip_matches)
            url_matches = url_pattern.findall(line)
            url_set.update(url_matches)
            if error_code_pattern.search(line):
                error_lines.append(line.strip())
    
    print(f"Количество запросов с каждого IP-адреса:")
    for ip, count in ip_counter.items():
        print(f"{ip}: {count}")
    
    print("\nУникальные URL-адреса:")
    for url in url_set:
        print(url)
    
    print("\nСтроки с ошибками:")
    for error in error_lines:
        print(error)

analyze_log('log1.log')
