# Software

En este carpeta se encuentran los codigos asoiados a cada entrega, ademas del codigo principal del proyecto el cual consta de la interfaz de ususario y la comunicacion con el micro. Toda esta parte del proyecto se encuentra implemnetada en python    
 
Los codigo aquiimplementados poseen la siguiene descripción:

+ Comunicacion_serial.py: En este modulo se implementa la aplicacion de PC, la cual se encarga de comunicarse con el microproesador y optener la informacion de los sensores, a partir e aqui la misma sigue un algoritmo que automatiza la acciones de salida deendiendo de las entradas que este recibe, toda la informacion relevante para el usuario e mostrada atravez de una inetrefaz grafica.

+ python_serial.py: Modulo imlementado para la primera entrega el cual fue la primera aproximamion a la hora de adquiriri los datos provenientes para la primera entrega

+ Grafica_offline.py: Modulo implementado para graficar la informacion adquirida por el microprocesador, la cual proviene del generador de funciones y posee una frcuencia de 1kHZ y es muestreada a 2kHz. 

+ Grafica_online.py: La señal proveniente del generador de funciones muestreada a 2kHz con una frecuencia de 1Khz adquirida por el microprocesador es procesada graficada en la pantalla de la computadora en tiempo pseudo real, es decir se ve de manera acontinua aunque obviamente los datos no se muestran en tiempo real.   

+ Enviar_datos.py: Codigo impementado para realizar envio de paquetes al microprocesador, como una primera aproximcion, para posteriormente en el modulo principla activar las salidas del sistema.    
