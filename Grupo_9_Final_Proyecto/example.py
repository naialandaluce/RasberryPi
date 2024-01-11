import RPi.GPIO as GPIO
from seeed_dht import DHT
from grove_rgb_lcd import *
import time
import Adafruit_DHT
from GPS import *
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
##AQUI LO QUE QUERIA HACER ES QUE SALIESE POR PANTALLLA
## LA HUMEDAD SI LE DIESE AL BOTON CAMBIARA AL RECORRIDO
##DESPUES TAMBIUEN COGIERA LAS PULSACIONES

SENSOR = Adafruit_DHT.DHT22
SENSOR_PIN = 22 # Cambia esto por el pin GPIO al que está conectado tu sensor

##Tenia pensado Programar la humedad
def leer_humedad_temperatura():
    humedad, temperatura = Adafruit_DHT.read_retry(SENSOR, SENSOR_PIN)
    if humedad is not None and temperatura is not None:
        return f"Temp: {temperatura:.1f}C, Hum: {humedad:.1f}%"
    else:
        return "Error de lectura"
 
 
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))        
def leer_pulsaciones():
    # Leer del canal donde está conectado el sensor
    valor = mcp.read_adc(CANAL_DEL_SENSOR)
    # Convertir este valor a pulsaciones por minuto (bpm)
    # Este paso depende de cómo tu sensor codifica las pulsaciones en la señal analógica
    bpm = convertir_a_bpm(valor)
    return bpm       
# Configura el modo GPIO y define el pin del botón
GPIO.setmode(GPIO.BCM)
BUTTON_PIN = 16
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Información para mostrar
# Información de las distancias de las rutas para mostrar
informacion = [
    f"Ruta 1: {distance_1:.2f} km",
    f"Ruta 2: {distance_2:.2f} km",
    f"Ruta 3: {distance_3:.2f} km",
    f"Ruta 4: {distance_4:.2f} km",
    # ...  tenia 8 rutas pero solo he puesto 4 por que no funcionaba 
]

indice_informacion = 0


# Función para actualizar la pantalla LCD
def actualizar_lcd():
    global indice_informacion
    setText(informacion[indice_informacion])
    setRGB(0,128,64)


# Añade la función de lectura del sensor de pulsaciones a la lista de información
informacion.append(leer_pulsaciones)
informacion.append(leer_humedad_temperatura)

# Modifica la función boton_presionado para incluir la nueva información
def boton_presionado(channel):
    global indice_informacion
    indice_informacion = (indice_informacion + 1) % len(informacion)
    if callable(informacion[indice_informacion]):
        display_text = informacion[indice_informacion]()
    else:
        display_text = informacion[indice_informacion]
    actualizar_lcd(display_text)


# Añade un evento de detección de borde descendente al botón
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=boton_presionado, bouncetime=300)

# Inicializa la pantalla con la primera información
actualizar_lcd()

# Bucle principal para mantener el programa en ejecución
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    # Limpia los recursos al salir
    setText('')
    setRGB(0,0,0)
    GPIO.cleanup()
