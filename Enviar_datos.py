import serial
demoqe = serial.Serial('COM3', 9600, timeout=1)
demoqe.close()

while True:
    dato = input()
    print(type(dato))
    dato = bytes(dato,'utf-8')
    demoqe.write(dato)
    print(dato)