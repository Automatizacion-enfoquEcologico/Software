import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import serial, time

demoqe = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2) #Tiempo de inicializacion del puerto serial
#demoqe.write('k') # envia 'k' y recibe 'a', falta configurar un imput o entrada de teclado
#rawString = demoqe.readline(2)
#b = ord(rawString) -255



COUNT = 1000
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_ylim([0, 256])
ax.set_xlim(0, COUNT)
y = 0
xdata = []
ydata = []
def next():
   i = 0
   while i <= COUNT:
      i += 1
      yield i
def update(i):
   xdata.append(i)
   global y
   rawString = demoqe.read(2)
   # print(len(rawString))
   if len(rawString) == 2:
      recibido = list(rawString)
      # print(int(ord(recibido[0])))
      if (int(ord(recibido[0]))) == 255:
         y = int(ord(recibido[1]))


   print (y)
   print (rawString)
   ydata.append(y)
   line.set_data(xdata, ydata)
   return line,
if __name__ == '__main__':
   a = animation.FuncAnimation(fig, update, next, blit = False, interval = 60,
                               repeat = False)
   plt.show()

demoqe.close()