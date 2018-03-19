import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


demoqe = serial.Serial('COM3', 115200, timeout=1)
demoqe.set_buffer_size(5,1)
COUNT = 1500
y = []
x = []
i = 0

while i <= COUNT:
    i += 1
    mensaje = demoqe.read(5)
    mensaje=list(mensaje)
    print (mensaje)
    y.append(mensaje[1])
    x.append(i)


plt.plot(x,y)
plt.show()
demoqe.close()
