'''Задача 1: Анализ текста и статистика
Напишите программу, которая считывает текстовый файл и выводит следующую информацию:
Общее количество строк в файле.
Общее количество слов в файле.
Топ-10 наиболее часто встречающихся слов, игнорируя регистр (слова вида "the" и "The" считаются одним и тем же словом).
Выводит все строки, в которых встречается слово, введенное пользователем.'''
from collections import Counter
import re as p
text = ""
count = 0
with open(r"A:\readme.txt", 'rb') as file:
    for line in file:
        text += ""+line.decode('unicode_escape')+"\n"
        count+=1
def task1(text):
    parameter = p.findall(r"\b\w+\b", text)
    count_words = len(parameter)
    meet_word = Counter(p.findall(r"\b[a-zA-Z]{2,}\b", text))
    sorted_words = sorted(meet_word)
    return count_words, sorted_words[:10]

def task2(text, slovo):
    out = ""
    for line in text.splitlines():
        if slovo in line:
            out += f"{line}\n"
    return out

output1,output2 = task1(text)
out_text = ", ".join(output2)
print(f"Количество строк {count}, количество слов {output1}, наиболее встречаемые слова - {out_text}")
print(f"Текст с предложениями с введенным словом: {task2(text, "Also")}")


'''
Версия chatgpt
from collections import Counter
import re

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def analyze_text(text):
    words = re.findall(r"\b\w+\b", text.lower())
    count_words = len(words)
    word_counter = Counter(words)
    most_common_words = word_counter.most_common(10)
    return count_words, most_common_words

def find_lines_with_word(text, word):
    word_pattern = re.compile(rf'\b{word}\b', re.IGNORECASE)
    lines_with_word = [line for line in text.splitlines() if word_pattern.search(line)]
    return "\n".join(lines_with_word)

# Основной код
text = read_file(r"A:\readme.txt")
line_count = text.count('\n') + 1
word_count, top_words = analyze_text(text)
word_to_search = "Also"  # Замените на ввод пользователя, если требуется

print(f"Количество строк: {line_count}")
print(f"Количество слов: {word_count}")
print(f"Топ-10 наиболее часто встречающихся слов: {', '.join([f'{word} ({count})' for word, count in top_words])}")

lines_with_word = find_lines_with_word(text, word_to_search)
print(f"Текст с предложениями, содержащими слово '{word_to_search}':\n{lines_with_word}")

'''