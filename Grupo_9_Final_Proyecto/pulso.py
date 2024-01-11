from gpiozero import Button
import RPi.GPIO as GPIO
from seeed_dht import DHT
from grove_rgb_lcd import *
import time
import Adafruit_DHT
from datetime import datetime
# Configura el pin del pulsómetro (ajusta el número de acuerdo a tu conexión)
pulsometro = DHT('11', 18)#Ejemplo con el pin GPIO 17

# Inicializa variables
contador_pulsaciones = 0
ultima_lectura = time.time()

try:
    while True:
        # Espera hasta que se detecte una pulsación
        pulsometro.wait_for_press()
        
        # Incrementa el contador de pulsaciones
        contador_pulsaciones += 1
        
        # Imprime las pulsaciones y la frecuencia cardíaca promedio
        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - ultima_lectura
        frecuencia_cardiaca_promedio = contador_pulsaciones / (tiempo_transcurrido / 60)  # Pulsaciones por minuto
        print(f'Pulsaciones: {contador_pulsaciones}, Frecuencia Cardíaca Promedio: {frecuencia_cardiaca_promedio:.2f} bpm')
        
        # Actualiza el tiempo de la última lectura
        ultima_lectura = tiempo_actual

except KeyboardInterrupt:
    print('Programa detenido')

