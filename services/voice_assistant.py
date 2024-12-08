import asyncio
import pyttsx3
import speech_recognition as sr
import random
import datetime
from datetime import date
from utils.audio_processing import speak
from utils.clima_processing import ReadClimate
from utils.read_file import ReadFile

def start_voice_assistant():
    saludo()
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("Asistente de voz iniciado. Di 'salir' para terminar.")
    sayRoberto = False
    
    while True:
        try:
            with mic as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                print("Audio capturado.")
                
            text = recognizer.recognize_google(audio, language="es-ES").lower()
            print(f"Texto detectado: {text}")
                            
            if 'oye roberto' in text:
                talk("¿En qué puedo ayudarte?")
                
            if 'ayuda' in text or 'opciones' in text:
                talk("Dispongo de muchas funciones, como obtener la temperatura o la humedad de hoy o la media de esta semana, también puede finalizar diciendo salir")

            if 'temperatura' in text:
                if 'hoy' in text:
                    now = date.today()
                    arrTemp, arrHumidity = getHoyClima()
                    if str(now) == arrTemp[0][0]:
                        talk( f"Hoy la temperatura es de {arrTemp[0][1]} grados.")
                    else:
                        talk(fraseNoRegistro('temperatura', 'hoy'))

                elif 'semana' in text:
                    arrTemp, arrHumidity = getHoyClima()
                    promedio = calcMediaSemana(arrTemp)
                    talk(f"La temperatura media de esta semana ha sido {promedio:.2f} grados.")

            elif 'humedad' in text:
                arrTemp, arrHumidity = getHoyClima()
                if 'hoy' in text:
                    talk(f"Hoy hay un {arrHumidity[0][1]}% de humedad.")
                elif 'semana' in text:
                    promedio_humedad = calcMediaSemana(arrHumidity)
                    talk(f"La humedad media de esta semana es {promedio_humedad:.2f}%.")

            elif 'ambas' in text:
                arrTemp, arrHumidity = getHoyClima()
                if 'hoy' in text:
                    talk(f"Hoy la temperatura es de {arrTemp[0][1]} grados y la humedad es del {arrHumidity[0][1]}%.")
                elif 'semana' in text:
                    promedio_temp = calcMediaSemana(arrTemp)
                    promedio_humedad = calcMediaSemana(arrHumidity)
                    talk(f"Para esta semana, la temperatura media es {promedio_temp:.2f} grados y la humedad media es {promedio_humedad:.2f}%.")
            
            elif 'salir' in text:
                talk("¡Adiós! Que tenga un excelente día.")
                stop = True
            
            else:
                talk("Lo siento, no entendí su solicitud. Por favor, intentelo de nuevo.")
    
        except Exception as e:
            print(f"Error al escuchar: {e}")

def fraseNoRegistro(unidad, fecha):
    return f'No hay ningún registro de la {unidad} de {fecha}'


def getHoyClima():
    try:
        clima = ReadClimate("data/out_shellyht.json")
        arrTemp, arrHumidity = clima.getClima()

        if not arrTemp or not arrHumidity:
            print("No se encontraron datos de clima en el archivo.")
            return None

        return arrTemp, arrHumidity

    except FileNotFoundError:
        print("Error: El archivo 'out_shellyht.json' no fue encontrado.")
        return None

    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

def calcMediaSemana(arr):
    total = 0
    i = 0
    j = 0
    while i < len(arr):
        if i == 0:
            total = float(arr[i][1])
        else:
            total += float(arr[i][1])
        i += 1

    media = float(total/len(arr))
    return media

def talk(msg):
    newVoiceRate = 180
    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[2])
    engine.setProperty('rate', newVoiceRate)
    engine.say(msg)
    engine.runAndWait()

def saludo():
    num = random.randint(0,9)
    if(num % 2 == 0):
        hour = datetime.datetime.now()
        if hour.hour < 6 or hour.hour > 20:
            momento = 'Buenas noches.'
        elif 6 <= hour.hour < 13:
            momento = 'Buenos días.'
        else:
            momento = 'Buenas tardes.'
        talk(f'{momento} Soy Roberto brasero, tu asistente personal. Por favor, dime en qué puedo ayudarte.')
    else:
        frases = ReadFile('config/frases.txt')
        arrFrases = frases.getArr()
        sizeArrFrases = len(arrFrases)
        talk(arrFrases[random.randint(0,sizeArrFrases-1)])
