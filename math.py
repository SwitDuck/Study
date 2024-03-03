'''
import math
def ctg(x):
    return math.cos(x) / math.sin(x)
def tg(x):
    return math.sin(x) / math.cos(x)
up = ctg(3.2)+math.sqrt(4+math.cos(1.3))
down = (math.cos(1.6)*math.pi-3*tg(2.8))**3
minus = -(math.e**(-5/9))*(1+math.cos(3*math.pi))
print((up/down)-minus)


import matplotlib as mpl
x = 1
y = 0.1
while y < 0.5:
    down1 = 1+(math.log(10,y)/(x+tg(y)))
    up1 = 1 + ((x+tg(y))/math.log(10,y))
    equal1=down**up
    
    y+=0.02

'''
import math
import matplotlib.pyplot as plt
import numpy as np

x = 1
y_values = []
equal_values = []

y = 0.1
while y <= 0.5:
    down1 = 1 + (np.log(y) / (x + np.tan(y)))
    up1 = 1 + ((x + np.tan(y)) / np.log(y))
    equal1 = np.power(down1, up1)
    y_values.append(y)
    equal_values.append(equal1)
    y = y + 0.02

# Построение графика
plt.plot(y_values, equal_values)
plt.xlabel('Значения y')
plt.ylabel('Значения W')
plt.title('График функции W(y) при x=1')
plt.grid(True)
plt.show()
