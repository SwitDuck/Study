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
