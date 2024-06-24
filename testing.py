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
