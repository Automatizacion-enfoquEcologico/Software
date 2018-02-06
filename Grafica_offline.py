import serial, time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


demoqe = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2) #Tiempo de inicializacion del puerto serial
COUNT = 1500
y = []
x = []
i = 0
while i <= COUNT:
    i += 1
    mensaje = demoqe.read(2)
    mensaje=list(mensaje)
    print (mensaje)
    y.append(mensaje[1])
    x.append(i)


plt.plot(x,y)
plt.show()
demoqe.close()
