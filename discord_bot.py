import discord
from discord.ext import commands
from gtts import gTTS
import os
import asyncio
from discord import FFmpegPCMAudio
import speech_recognition as sr
from utils.read_file import ReadFile
from utils.clima_processing import ReadClimate
from datetime import date

env = ReadFile('config/.env')
TOKEN =  str(env.getArr()[0].split("=")[1])

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True


bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        if ctx.guild.voice_client:
            await ctx.guild.voice_client.move_to(channel)
        else:
            vc = await channel.connect()
            await listen(vc)
            await ctx.send(f"Conectado al canal de voz: {channel}")
    else:
        await ctx.send("Debes estar en un canal de voz para usar este comando.")


@bot.command()
async def leave(ctx):
    if ctx.guild.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Desconectado del canal de voz.")

    else:
        await ctx.send("No estoy en un canal de voz.")


async def speak_in_voice_channel(message, text):
    tts = gTTS(text=text, lang='es')
    tts.save("speech.mp3")

    voice_client = message.guild.voice_client
    if voice_client:
        voice_client.play(FFmpegPCMAudio("speech.mp3"), after=lambda e: print("Reproducción terminada", e))
        while voice_client.is_playing():
            await asyncio.sleep(1)
    else:
        print("No estoy en un canal de voz")

    os.remove("speech.mp3")

async def listen(vc):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    stop = False
    sayRoberto = False
    while not stop:
        try:
            with mic as source:                
                recognizer.adjust_for_ambient_noise(source)
                audio = await asyncio.to_thread(recognizer.listen, source) # necesario para no bloquear el hilo
                print("Audio capturado.")

            text = recognizer.recognize_google(audio, language="es-ES").lower()
            print(f"Texto detectado: {text}")
            
            if 'ayuda' in text or 'opciones' in text:
                await speak_in_voice_channel(vc, "Dispongo de muchas funciones, como obtener la temperatura o la humedad de hoy o la media de esta semana, también puede finalizar diciendo salir")

            if sayRoberto:
                if 'temperatura' in text:
                    if 'hoy' in text:
                        now = date.today()
                        arrTemp, arrHumidity = await getHoyClima()
                        if str(now) == arrTemp[0][0]:
                            await speak_in_voice_channel(vc, f"Hoy la temperatura es de {arrTemp[0][1]} grados.")
                        else:
                            await speak_in_voice_channel(vc, fraseNoRegistro('temperatura', 'hoy'))
                            
                    elif 'semana' in text:
                        arrTemp, arrHumidity = await getHoyClima()
                        promedio = await calcMediaSemana(arrTemp)
                        await speak_in_voice_channel(vc, f"La temperatura media de esta semana ha sido {promedio:.2f} grados.")

                elif 'humedad' in text:
                    arrTemp, arrHumidity = await getHoyClima()
                    if 'hoy' in text:
                        await speak_in_voice_channel(vc, f"Hoy hay un {arrHumidity[0][1]}% de humedad.")
                    elif 'semana' in text:
                        promedio_humedad = await calcMediaSemana(arrHumidity)
                        await speak_in_voice_channel(vc, f"La humedad media de esta semana es {promedio_humedad:.2f}%.")

                elif 'ambas' in text:
                    arrTemp, arrHumidity = await getHoyClima()
                    if 'hoy' in text:
                        await speak_in_voice_channel(vc, f"Hoy la temperatura es de {arrTemp[0][1]} grados y la humedad es del {arrHumidity[0][1]}%.")
                    elif 'semana' in text:
                        promedio_temp = await calcMediaSemana(arrTemp)
                        promedio_humedad = calcMediaSemana(arrHumidity)
                        await speak_in_voice_channel(vc, f"Para esta semana, la temperatura media es {promedio_temp:.2f} grados y la humedad media es {promedio_humedad:.2f}%.")
                else:
                    await speak_in_voice_channel(vc, "Lo siento, no entendí su solicitud. Por favor, intentelo de nuevo.")
                
            if 'oye roberto' in text:
                await speak_in_voice_channel(vc, "¿En qué puedo ayudarte?")
                sayRoberto = True
                    
            elif 'salir' in text:
                await speak_in_voice_channel(vc, "¡Adiós! Que tenga un excelente día.")
                stop = True
        except Exception as e:
            print(f"Error al escuchar: {e}")

def fraseNoRegistro(unidad, fecha):
    return f'No hay ningún registro de la {unidad} de {fecha}'


async def getHoyClima():
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
    
async def calcMediaSemana(arr):
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


bot.run(TOKEN)
