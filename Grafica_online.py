import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


demoqe = serial.Serial('COM3', 115200, timeout=1)
demoqe.set_buffer_size(2,1)
demoqe.flushInput()
z = []
y = []
plt.ylim(0,50)
plt.xlim(0, 100)

while True:
    mensaje = demoqe.read(8)
    mensaje=list(mensaje)
    print(mensaje)
    y.append(50*mensaje[2]/255)
    z.append(mensaje[3]*50/255)
    plt.plot(z)
    plt.plot(y)
    plt.pause(0.000000001)


    if len(y) == 100:
        y.clear()
        z.clear()
        demoqe.reset_input_buffer()
        demoqe.flushInput()
        plt.clf()
        plt.ylim(0,50)
        plt.xlim(0,100
                 )