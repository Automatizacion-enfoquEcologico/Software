import serial
import pygame
import time

#demoqe = serial.Serial('COM3', 9600, timeout=1)



# Inicializacion de variables de maquina de estado
cabecera = str('255').encode()
estado = 0
recepcion = 0
enviar =  1
usuario =  2
salida = 0

#Inicializacion de interfaz grafica
WIDTH = 1280
HEIGHT = 720

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("DOMOTICA")
imagenfondo = pygame.image.load('casa_azul.png').convert_alpha()
imagentitulo = pygame.image.load('titulo.png').convert_alpha()
imagentermometro = pygame.image.load('termometro_prueba.png').convert_alpha()
imagencorriente = pygame.image.load('corriente_prueba.png').convert_alpha()
imagenluzno = pygame.image.load('luz_no.png').convert_alpha()
imagenluzmed = pygame.image.load('luz_med.png').convert_alpha()
imagenluzhigh = pygame.image.load('luz_high.png').convert_alpha()
imagengotanegra = pygame.image.load('gota_negra.png').convert_alpha()
imagengotaazul = pygame.image.load('gota_azul.png').convert_alpha()
clock = pygame.time.Clock()


#define colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

font_name = pygame.font.match_font('Berlin Sans FB Demi')

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect:__init__(seld,0,0,1,1)
    def update(self):
        self.left, self.top = pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
    def __init__(self, imagen, x, y):
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
        self.rect.center = (x,y)
    def update(self, screen, cursor):
        if cursor.colliderect(self.rect):
            self.imagen = self.imagen
        else:
            self.imagen = self.imagen
        screen.blit( self.imagen, self.rect)


def draw_text(screen, text, size, x, y, color):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text, True, WHITE)
    a,b = text_surface.get_size()
    a = a+10
    b = b+30
    surf = pygame.Surface((a,b))
    surf.fill(color)
    text_rect = text_surface.get_rect()
    text_rect.center = (a/2, b/2)
    text_surface.blit(text_surface,text_rect)
    surf_rect = surf.get_rect()
    surf_rect.center = (x,y)
    screen.blit(text_surface,surf_rect)

    return surf

def draw_sensors(screen, rawstring, LDR, Hig, Mag, Aire, PWM, Riego ):
    #Dibujar temperatura interna
    #caudal = 'Caudal: %s'%(str(int(rawstring[5])))
    #draw_text(screen,caudal,16,160,120,BLUE)
    screen.blit(imagentermometro, (0, 240))
    screen.blit(imagencorriente, (0, 500))
    temp1 = '%s C (Interna)'%(str(int(int(rawstring[2])*50/255)))
    draw_text(screen, temp1, 16, 230, 300,BLUE)
    temp2 = '%s C (Externa)'%(str(int(int(rawstring[3])*50/255)))
    draw_text(screen, temp2, 16, 230, 350, BLUE)
    corriente = '%s A '%(str(int(rawstring[4])))
    draw_text(screen, corriente, 16, 230, 585, BLUE)


    if Riego == 1:
        screen.blit(imagengotaazul, (1120, 120))
    else:
        screen.blit(imagengotanegra, (1120, 120))
    riego = 'Riego: %s'%(Riego)
    rig = draw_text(screen, riego, 16, 1120, 120, BLUE)
    boton1 = Boton(imagengotaazul, 1120, 120)
    aire = 'Aire: %s'%(Aire)
    air = draw_text(screen, aire, 16, 1120, 360, BLUE)
    boton2 = Boton(air, 1120, 360)

    if PWM == 0:
        screen.blit(imagenluzno, (1120, 600))
    if PWM == 127.5:
        screen.blit(imagenluzmed, (1120, 600))
    if PWM == 254.5:
        screen.blit(imagenluzhigh, (1120, 600))
    Pwm = 'PWM: %s'%(PWM)
    pwm = draw_text(screen, Pwm, 16, 1120, 600, BLUE)
    boton3 = Boton(imagenluzno, 1120, 600)

    return boton1, boton2, boton3

PWM = 0
Riego = '1'
#Game loop

cursor1 = Cursor()

running = True

while running:

    clock.tick(30)

    if estado == recepcion:
        #rawstring = demoqe.read(8)
        #rawstring = list(rawstring)
        rawstring = [255, 178, 255, 125, 150, 167, PWM, 157]
        if int(rawstring[0]) == 255:
            estado = usuario

    if estado == enviar:

        PWM = str(PWM).encode()
        if Riego == '1':
            if Aire == '1':
                Arig = 3
            else:
                Arig = 2
        else:
            if Aire == '1':
                Arig = 1
            else:
                Arig = 0

        Arig = str(Arig).encode()
        demoqe.write(cabecera)
        demoqe.write(PWM)
        demoqe.write(Arig)

        estado = recepcion




    if estado == usuario:

        sensores_digitales = int(rawstring[1])
        sensores_digitales = bin(sensores_digitales)
        sensores_digitales = list(sensores_digitales)

        LDR = (sensores_digitales[5:7])
        LDR1 = LDR[0]
        LDR0 = LDR[1]
        if LDR1 == '1':
            if LDR0 == '1':
                LDR = 'HIGH'
            else:
                LDR = 'MED'
        else:
            LDR = 'LOW'


        Hig = sensores_digitales[7]
        if Hig == '1':
            Hig = 'Regar'
        else:
            Hig = 'No regar'


        Mag = sensores_digitales[8]
        if Mag == '1':
            Mag = 'Puerta abierta'
        else:
            Mag = 'Puerta cerrada'


        PIR = sensores_digitales[9]
        if PIR == '1':
            PIR = 'ACT'
        else:
            PIR = 'NO ACT'

        salidas_digitales = int(rawstring[7])
        salidas_digitales = bin(salidas_digitales)
        salidas_digitales = list(salidas_digitales)

        #Riego = Riego #salidas_digitales[3]
        if Riego == '1':
            Riego = 1
        else:
            Riego = 0

        Aire = salidas_digitales[4]
        if Aire == '1':
            Aire = 'Encendido'
        else:
            Aire = 'Apagado'

        PWM = rawstring[6]

        #Tabla de comportamineto

        #LUZ = %s Higrometro: %s Puerta: %s Movimiento: %s'%(LDR,Hig,Mag,PIR,)
        Analogico = 'Temperatura 1: %s Temperatura 2: %s Corriente: %s Caudal: %s PWM: %s'%(str(int(rawstring[2])),str(int(rawstring[3])),str(int(rawstring[4])),str(int(rawstring[5])),str(int(rawstring[6])))
        estado = recepcion

    #Interfaz

    #Update


    #Draw / render

    screen.fill(BLUE)
    boton1, boton2, boton3 = draw_sensors(screen, rawstring, LDR, Hig, Mag, Aire, PWM, Riego)
    cursor1.update()

    #Process input

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            if cursor1.colliderect(boton1.rect):
                if Riego == 1:
                    Riego = 0
                else:
                    Riego = 1
                #estado = enviar
            if cursor1.colliderect(boton2.rect):
                if Aire == 'Encendido':
                    Aire = '1'
                else:
                    Aire = '0'
                #estado = enviar
            if cursor1.colliderect(boton3.rect):
                PWM = int(PWM) + 127.5
                if PWM > 255:
                    PWM = 0
                #estado = enviar
        #check for closing window
        if event.type == pygame.QUIT:
            running = False

    #*after* drawing everthing, flip the display
    screen.blit(imagenfondo,(440,210))
    #screen.blit(imagentitulo,(86,0))


    pygame.display.flip()


pygame.quit()
#demoqe.close()
