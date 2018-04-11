# Software:Comunicacion Serial- Aplicacion PC

## Descripción 
 En este módulo se implementa la aplicación de PC, la cual se encarga de comunicarse con el microprocesador y obtener la información de los sensores, a partir de aquí la misma sigue un algoritmo que automatiza la acciones de salida dependiendo de las entradas que este recibe, toda la información relevante para el usuario e mostrada atreves de una interfaz gráfica.

## Tabla de contenidos

- [Requisitos](#requisitos)
- [Software](#software)
- [License](#license)

## Requisitos
La aplicación fue desarrollada y probada en Windows 10 - 64 bits.
 - Python 3.6
 - Libreiras: Pyserial, Time, Pygame.
 
## Software
El desarrollo de la aplicacion fue realizado en el entorno PyCharm 2017.3.3.    

# Sofware variado:

+ python_serial.py: Modulo imlementado para la primera entrega el cual fue la primera aproximamion a la hora de adquiriri los datos provenientes para la primera entrega

+ Grafica_offline.py: Modulo implementado para graficar la informacion adquirida por el microprocesador, la cual proviene del generador de funciones y posee una frcuencia de 1kHZ y es muestreada a 2kHz. 

+ Grafica_online.py: La señal proveniente del generador de funciones muestreada a 2kHz con una frecuencia de 1Khz adquirida por el microprocesador es procesada graficada en la pantalla de la computadora en tiempo pseudo real, es decir se ve de manera acontinua aunque obviamente los datos no se muestran en tiempo real.   

+ Enviar_datos.py: Codigo impementado para realizar envio de paquetes al microprocesador, como una primera aproximcion, para posteriormente en el modulo principla activar las salidas del sistema.    
