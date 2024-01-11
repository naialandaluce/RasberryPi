import RPi.GPIO as GPIO
from seeed_dht import DHT
from grove_rgb_lcd import *
import time
import Adafruit_DHT
from datetime import datetime

import csv

def guardar_datos(humedad, temperatura):
    with open('datos_sensor.csv', 'a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([datetime.now(), humedad, temperatura])

# Configura el modo GPIO y el pin del botón
GPIO.setmode(GPIO.BCM)
BUTTON_PIN = 17
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

sensor = DHT('11', 22)

def actualizar_lcd():
    humi, temp = sensor.read()
    hora_actual = datetime.now().strftime("%H:%M:%S")  # Formato de 24 horas
    
    if humi is not None and temp is not None:
        setText('9KM    {}\nT:{:.1f}C, H:{:.1f}%'.format(hora_actual, temp, humi))
        setRGB(0,128,64)
        guardar_datos(humi, temp)  
    else:
        setText('Error de lectura')

# Función de callback para el botón
#def boton_presionado(channel):
#    actualizar_lcd()

# Añade detección de evento para el botón
#GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=boton_presionado, bouncetime=200)

# Inicializa la pantalla LCD
#actualizar_lcd()

# Bucle para mantener el programa en ejecución
try:
    while True:
        actualizar_lcd()
        time.sleep(2)  # Espera 2 segundos antes de la próxima actualización
except KeyboardInterrupt:
    setText('')
    setRGB(0,0,0)
    GPIO.cleanup()
