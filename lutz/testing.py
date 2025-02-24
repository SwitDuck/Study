'''
D = {'a':1, 'b':2}
F=open('datafile.pkl', 'wb')
import pickle
pickle.dump(D,F)
F.close()
F = open('datafile.pkl','rb')
E = pickle.load(F)
print(E)
'''
'''
import struct
F = open('data.bin', 'wb')
data = struct.pack('>i4sh', 7, b'spam', 8)
F.write(data)
F.close()
F = open('data.bin', 'rb')
data = F.read()  
F.close()
values = struct.unpack('>i4sh', data)
print(values)
'''
'''
X = [1, 2, 3]
L = ['a', X, 'b']
D = {'x':X,'y':2}
X[1]='surprise'
print(L)
print(D)
'''
'''while True:
    reply = input('enter text:')
    if reply == 'stop': break
    try:
        num = int(reply)
    except:
        print('bad'*8)
    else:
        print(int(reply)**2)
print('bye')'''


'''x,y,z = 'параметры', 'установки', 'windows'
print(x,y,z, sep=', ', end='!\n', file=open('data.txt', 'w'))
print(open('data.txt').read())'''
#пример использования else в цикле while
'''y = 4
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is prime')'''
'''import re as r
found = False; x = [5,1,4,12,8,7,3,24]
while x and not found:
    if r.match(x[0]):
        print('Ni')
        found = True
    else:
        x = x[1:]
if not found:
    print('not found')

while x:
    if r.match(x[0]):
        x = x[1:]
else:
    print('not found')'''
'''file = open('data1.txt', 'rb')
while True:
    chunk = file.read(10)
    if not chunk: break
    print(chunk)
file.close()'''

'''S = 'abcdefghijk'
list(range(0, len(S), 2))
for i in range(0, len(S), 2): print(S[i], end=' ')'''
'''
L = [1,2,3]
I = iter(L)
print(I.__next__())'''

'''
L = [1,2,3]
for X in L:
    print(X**2, end=' ')

I = iter(L)
while True:
    try:
        X = next(I)
    except StopIteration:
        break
    print(X**2, end=' ')
'''

'''
D = {'a':1,'b':2,'c':3}
for key in D.keys():
    print(key,D[key])
'''
'''
D = {'a':1,'b':2,'c':3}
#for key in D.keys():
#    print(key,D[key])
I = iter(D)
print(next(I))
print(next(I))
print(next(I))
E = enumerate('spam')
print(E)
I = iter(E)
print(next(I))
l1 = list(enumerate('spam'))
print(l1)
'''

'''
#функции итерации для вычисления
#max и min работают и для файлов и для строк для нахождения наиб и наим колво символов
print(
sum([6, 1, -5, 3, 10, -2]),
max([6, 1, -5, 3, 10, -2]),
min([6, 1, -5, 3, 10, -2]),
any(['spam', '', 'ni']),
all(['spam', '', 'ni'])
)'''

'''
#{ix: line for (ix, line) in enumerate(open('script1.py')) if line[0]=='p'}

import string
print(dir(string))
'''

'''
#что то непонятное
text = "slovo"
new_text = ''
sum = 0
for i in text:
    new_text+=str(ord(i))
    sum += ord(i)
print(new_text)
print(sum)
map(ord, )
'''
'''
var = 99
def local():
    var = 0
def glob1():
    global var
    var += 1
def glob2():
    var = 0
    import testing
    testing.var += 1
def glob3():
    var = 0
    import sys
    glob = sys.modules['testing']
def test():
    print(var)
    local(); glob1(); glob2(); glob3();
    print(var)
test()'''

'''
def clovar(**kwargs):
    for name, value in kwargs.items():
        print(name,value)
clovar(value1=1, value2=2, value3=3)
mydict = {'foo':1,'bar':2}
clovar(**mydict)'''

'''def edition():
    x=10
    def edit():
        X = 20
        nonlocal x 
        x+=10
        print(x)
        return X
    return edit()
print(edition())'''
'''
class C2: ...
class C3: ...
class C1(C2, C3):
    def setname(self, who):
        self.name = who
I1 = C1()
I2 = C1()
I1.setname('BOB')
I2.setname('SUE')
print(I1.name)'''
'''
В текущем виде наш класс С1 не присоединяет атрибут name к экземпляру до тех 
пор, пока не будет вызван метод setname. В действительности ссылка II .name перед 
вызовом II. setname привела бы к возникновению ошибки неопределенного имени. 
'''
'''class C2: ...
class C3: ...
class C1(C2, C3):
    def __init__(self, who):
        self.name = who
I1 = C1('BOB')
I2 = C1('SUE')
print(I1.name)'''
'''
Каждый раз, когда экземпляр генерируется из класса, Python автоматически вы­
зывает метод по имени__ init__ , будь он реализован или унаследован. Как обычно,
новый экземпляр передается в аргументе self метода__ init__ , а значения, пере­
численные в круглых скобках при обращении к классу, передаются второму и после­
дующим аргументам. Результатом оказывается инициализация экземпляров,
'''
