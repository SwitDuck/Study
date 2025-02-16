#ex1 guessing game
'''import random
def guessing_game(): #Этот вариант не подходит из за рекурсии и генерации новых случайных значений
    random_parameter = random.randint(0,100)
    user_parameter = int(input("Введите значение которое выбрано случайно(0-100): "))
    if random_parameter == user_parameter:
        print("right number")
    elif random_parameter < user_parameter:
        print("too high")
        return guessing_game()
    else:
        print("too low")
        return guessing_game()'''
'''
import random
def guessing_game1():
    random_parameter = random.randint(0,100)
    while True:
        def vvod():
            user_input = input("Введите число (используйте 0b для двоичных, 0x для шестнадцатеричных, иначе считается десятичным): ")
            if user_input.startswith("0b"):  # Двоичное число
                number = int(user_input, 2)
                return number
            elif user_input.startswith("0x"):  # Шестнадцатеричное число
                number = int(user_input, 16)
                return number
            else:  # Десятичное число
                number = int(user_input)
                return number
        user_parameter = vvod()
        if random_parameter == user_parameter:
            print("right number")
            return False
        elif random_parameter < user_parameter:
            print("too high")
        else:
            print("too low")
guessing_game1()'''

#ex2 написание собственной функции sum
'''
def my_sum(*args):
    n = args[0]
    for i in args[1:]:
        n = i + n
    return n
print(my_sum(1,2,3,4,5,6,7))
'''

'''
address = "155.155.155.155"
new_address = address.replace(".", "[.]")
'''

'''
def minOperations(boxes):
    n = len(boxes)
    1 <= n <= 1000
    bin(boxes)
'''
#ex38 создание классов
'''
class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor
def create_scoops():
    scoops = [Scoop('chocolate'), Scoop('vanila'), Scoop('persimmon')]
    for scoop in scoops:
        print(scoop.flavor)
create_scoops()
class Beverage(Scoop):
    def __init__(self, flavor, temperature=None):
        default_temperature = 75
        super().__init__(flavor)
        if temperature is not None:
            self.temperature = temperature
        else: self.temperature = default_temperature
def create_beverage():
    scoops = [Beverage("chocolate", "-10"), Beverage("vanila", "-9"), Beverage("persimmon")]
    for scoop in scoops:
        print(scoop.flavor, scoop.temperature)
create_beverage()
class LogFile():
    def __init__(self, file):
        self.file = file
def file_open():
    path = "A://"
    with open (path, "w") as file:
        file.write(LogFile(file))
file_open()
class LogFile1:
    def __init__(self, filename):
        self.file = open(filename, "w")  # Открываем файл на запись
    def write(self, text):
        self.file.write(text + "\n")  # Записываем строку
    def close(self):
        self.file.close()  # Закрываем файл
# Использование класса
log = LogFile("log.txt")  # Создаём файл log.txt
log.write("Первая запись в лог")  # Записываем строку
log.write("Вторая запись в лог")
log.close()  # Закрываем файл
'''
#ex 39 композиция
'''class bowl():
    def __init__(self):
        self.scoops = []
    def add_scoop(self, scoop):
        self.scoops.append(scoop)
b = bowl()
b.add_scoop("chocolate")
print(b.scoops)

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    def __init__(self):
        self.scoops = [] 
    def add_scoops(self, *new_scoops): 
        for one_scoop in new_scoops:
            self.scoops.append(one_scoop)
    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops) 

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b)'''
'''
Create a Book class that lets you create books with a title, author, and price.
Then create a Shelf class, onto which you can place one or more books with an
add_book method. Finally, add a total_price method to the Shelf class, which
will total the prices of the books on the shelf.
'''
'''
class Book():
    def __init__(self, title, author, price, width):
        self.title = title
        self.author = author
        self.price = int(price)
        self.width = int(width)
class Shelf():
    def __init__(self, width = 60):
        self.books = []
        self.width = width
    def add_book(self, *books, ):
        for book in books:
            if (book.width < self.width):
                self.books.append(book)
                self.width -= book.width
            else:
                raise Exception("Слишком толстая книга")
    def total_prices(self):
        return sum(int(book.price) for book in self.books)
    def has_book(self, name):
        return any(book.title == name for book in self.books)
b1 = Book('seven', 'armies', '23', '35')
b2 = Book('Resident', 'Evil', '7', '24')
shelf = Shelf()
shelf.add_book(b1, b2)
print(f"Общая стоимость книг в шкафу - {shelf.total_prices()}")
'''
'''
 Write a method, Shelf.has_book, that takes a single string argument and
returns True or False, depending on whether a book with the named title
exists on the shelf.
'''
'''print(f'есть ли книга seven в шкафу - {shelf.has_book('seven')}')'''
#ex40
''' 
Define a Person class, and a population class attribute that increases each time
you create a new instance of Person. Double-check that after you’ve created five
instances, named p1 through p5, Person.population and p1.population are
both equal to 5.

Python provides a __del__ method that’s executed when an object is garbage
collected. (In my experience, deleting a variable or assigning it to another
object triggers the calling of __del__ pretty quickly.) Modify your Person class
such that when a Person instance is deleted, the population count decrements
by 1. 

Define a Transaction class, in which each instance represents either a deposit or a
withdrawal from a bank account. When creating a new instance of Transaction,
Uses Bowl.max_scoops to get the maximum per bowl, set on the class
'''
'''
import gc
class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor
        self.max_scoops = 3
class Bowl():
    def __init__(self):
        self.scoops = [] 
    def add_scoops(self, *new_scoops): 
        for one_scoop in new_scoops:
            if (len(self.scoops) <= self.max_scoops):
                self.scoops.append(one_scoop)
            else:
                self.scoops = self.scoops
    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)
class Person():
    population = 0
    def __init__(self, person, age):
        self.name = person
        self.age = age
        Person.population += 1
    def __del__(self):
        Person.population -= 1
'''
#ex 41
'''
Write an Envelope class, with two attributes, weight (a float, measuring grams)
and was_sent (a Boolean, defaulting to False). There should be three meth-
ods: (1) send, which sends the letter, and changes was_sent to True, but only
after the envelope has enough postage; (2) add_postage, which adds postage
equal to its argument; and (3) postage_needed, which indicates how much
postage the envelope needs total. The postage needed will be the weight of the
envelope times 10. Now write a BigEnvelope class that works just like Envelope
except that the postage is 15 times the weight, rather than 10.

Create a Phone class that represents a mobile phone. (Are there still nonmobile
phones?) The phone should implement a dial method that dials a phone num-
ber (or simulates doing so). Implement a SmartPhone subclass that uses the
Phone.dial method but implements its own run_app method. Now implement
an iPhone subclass that implements not only a run_app method, but also its
own dial method, which invokes the parent’s dial method but whose output is
all in lowercase as a sign of its coolness.

Define a Bread class representing a loaf of bread. We should be able to invoke a
get_nutrition method on the object, passing an integer representing the
number of slices we want to eat. In return, we’ll receive a dict whose key-value
pairs will represent calories, carbohydrates, sodium, sugar, and fat, indicating
the nutritional statistics for that number of slices. Now implement two new
classes that inherit from Bread, namely WholeWheatBread and RyeBread. Each
class should implement the same get_nutrition method, but with different
nutritional information where appropriate.
'''
'''
class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor
class Bowl():
    def __init__(self):
        self.scoops = []
        self.max_scoops = 3
    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if (len(self.scoops) <= self.max_scoops):
                self.scoops.append(one_scoop)
            else:
                self.scoops = self.scoops
    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)
class BigBowl(Bowl):
    def __init__(self):
        self.max_scoops = 5

class Envelope:
    def __init__(self, weight, was_sent=False):
        self.weight = weight
        self.was_sent = was_sent
        self.postage = 0
    def send(self):
        if self.postage >= self.postage_needed():
            print("Отправлено письмо")
            self.was_sent = True
        else:
            print("Недостаточно марок для отправки!")
    def add_postage(self, amount):
        self.postage += amount
    def postage_needed(self):
        return self.weight * 10
class BigEnvelope(Envelope):
    def postage_needed(self):
        return self.weight * 15
        
class Phone():
    def __init__(self, name, number, sim = "89140001122"):
        self.sim = sim
        self.name = name
        self.number = number
        self.contacts = []
    def add_contact(self, *contact_list):
        for item in contact_list:
            self.contacts.append(item)
        return contact_list
    def dial(self, name):
        for contact in self.contacts:
            if contact[0] == name:  # Ищем по имени
                print(f'Попытка соединения {self.sim} → {contact[0]} ({contact[1]})')
                return
        print(f'Контакт {name} не найден в списке контактов.')
phone = Phone("Иван", "89141234567")  # Создаём телефон
phone.add_contact(["Анна", "89215556677"], ["Сергей", "89337778899"])
phone.dial("Анна")
phone.dial("Павел")'''
#ex 42 Flexible dict
'''
class FlexibleDict(dict):
    def __getitem__(self, key):
        if key in self.items():
            try:
                if key == str:
                    return super().__getitem__(int(key))
                elif key == int:
                    return super().__getitem__(str(key))
            except:
                print('Неприводимый тип данных')
        else: return super().__getitem__(key)
class FlexibleDict1(dict):
    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)
        try:
            alt_key = str(key)
            if alt_key in self:
                return super().__getitem__(alt_key)
            alt_key = int(key)
            if alt_key in self:
                return super().__getitem__(alt_key)
        except ValueError:
            pass
        return super().__getitem__(key)
'''
'''С помощью FlexibleDict мы позволили пользователю использовать любые ключи, но сделали процесс извлечения данных более
гибким. Теперь реализуйте StringKeyDict, который будет конвертировать все ключи в строки при добавлении новых элементов. 
Таким образом, после выполнения skd[1] = 10 вы сможете обратиться к skd['1'] и получить значение 10. 
Это может быть полезно, если ключи читаются из файла, где невозможно заранее определить, будут они строками или числами.

Класс RecentDict должен работать так же, как обычный dict, но хранить ограниченное количество пар "ключ-значение",
 заданное при создании объекта. Например, RecentDict(5) будет сохранять только последние 5 пар, удаляя самые старые при
 добавлении новых. Важно учитывать, что современные dict в Python сохраняют порядок добавления элементов.

Класс FlatList должен наследоваться от list и переопределять метод append. Если в append передан итерируемый объект, 
то его элементы добавляются по отдельности, а не как один элемент.
Например, fl.append([10, 20, 30]) должно добавить в список fl три числа: 10, 20, 30, а не сам список [10, 20, 30].
Для проверки, является ли объект итерируемым, можно использовать встроенную функцию iter().'''
class StringKeyDict(dict):
    def __getitem__(self, key):
        try:
          alt_key = str(key)
          return super().__getitem__(alt_key)
        except ValueError:
          print('An exception occurred')
        return super().__getitem__(key)
a = StringKeyDict()
a[1] = 10
print(a['1'])

