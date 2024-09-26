'''import itertools
def recover_secret(triplets):
    def count_symv(triplets):
        uniq_symv = []
        for item in triplets:
            for i in item:
                if i not in uniq_symv:
                    uniq_symv.append(i)
        return len(uniq_symv), uniq_symv
    def valid_text(text, vowels):
        for i in range(2, len(text)):
            if text[i] in vowels and text[i-1] in vowels and text[i-2] in vowels:
                return False
            if text[i] in vowels and text[i-1] in vowels:
                return False
        return True
    def generate_text(length, symbols):
        vowels = ['a', 'e', 'i', 'o', 'u']
        for permutation in itertools.permutations(symbols, length):
            if valid_text(permutation, vowels):
                return ''.join(permutation)
        return None
    length, uniq_symb = count_symv(triplets)
    return generate_text(length, uniq_symb)
    
triplets = [
          ['t','u','p'],
          ['w','h','i'],
          ['t','s','u'],
          ['a','t','s'],
          ['h','a','p'],
          ['t','i','s'],
          ['w','h','s']]
print(recover_secret(triplets))
'''

from collections import defaultdict, deque

def recover_secret(triplets):
    # Построим граф зависимостей и подсчитаем входящие рёбра
    graph = defaultdict(set)  # Граф зависимостей
    in_degree = defaultdict(int)  # Счётчик входящих рёбер (какие символы перед какими)
    
    # Инициализация графа на основе триплетов
    for triplet in triplets:
        for i in range(2):
            if triplet[i+1] not in graph[triplet[i]]:
                graph[triplet[i]].add(triplet[i+1])
                in_degree[triplet[i+1]] += 1
            if triplet[i] not in in_degree:
                in_degree[triplet[i]] = 0  # Убедимся, что символ инициализирован в in_degree
    
    # Ищем символы с нулевой степенью входа
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    secret = []

    # Выполняем топологическую сортировку
    while queue:
        char = queue.popleft()
        secret.append(char)
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ''.join(secret)
triplets1 = [
    ['j', 'o', 'i'],
    ['o', 'i', 'n'],
    ['i', 'n', 'c'],
    ['n', 'c', 'l'],
    ['c', 'l', 'u'],
    ['l', 'u', 'b']
]

# Пример использования:
triplets = [
          ['t','u','p'],
          ['w','h','i'],
          ['t','s','u'],
          ['a','t','s'],
          ['h','a','p'],
          ['t','i','s'],
          ['w','h','s']]

print(recover_secret(triplets1)) 
