import serial, time


demoqe = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2) #Tiempo de inicializacion del puerto serial
demoqe.close()
for i in range(1,100000):
	rawString = demoqe.read(2)
	#print(len(rawString))
	if len(rawString) == 2:
		recibido = list(rawString)
		#print(int(ord(recibido[0])))
		if (int(ord(recibido[0]))) == 255:
			print(int(ord(recibido[1])))
	
		

demoqe.close()
