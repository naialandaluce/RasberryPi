import RPi.GPIO as GPIO
from grove_rgb_lcd import *
import time


##AQUI LO QUE HE HECHO HA SIDO METER LAS RUTAS QUE HEMOS HECHO EN EL GPS 
##y QUE APAREZZCAN POR PANTALLA


# Importa tu script GPS.py o copia las funciones necesarias aquí
import GPS

# Supongamos que tienes una función en GPS.py que devuelve las distancias
# Por ejemplo, distances = GPS.calculate_distances()
import RPi.GPIO as GPIO
# Configura el modo GPIO y define el pin del botón

distancias_rutas = [
    f"Ruta 1: {distance_1:.2f} km",
    f"Ruta 2: {distance_2:.2f} km",
    f"Ruta 3: {distance_3:.2f} km",
    # Añade más rutas según sea necesario
]

# Configura el modo GPIO y define el pin del botón
GPIO.setmode(GPIO.BCM)
BUTTON_PIN = 17
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

indice_actual = 0

# Función para actualizar la pantalla LCD
def actualizar_lcd():
    setText(distancias_rutas[indice_actual])
    setRGB(0,128,64)

# Función de callback para el botón
def boton_presionado(channel):
    global indice_actual
    indice_actual = (indice_actual + 1) % len(distancias_rutas)
    actualizar_lcd()

# Añade un evento de detección de borde descendente al botón
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=boton_presionado, bouncetime=200)

# Inicializa la pantalla con la primera ruta
actualizar_lcd()

# Bucle principal para mantener el programa en ejecución
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    setText('')
    setRGB(0,0,0)
    GPIO.cleanup()
