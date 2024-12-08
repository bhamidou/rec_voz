# Asistente de Voz con Python

Este proyecto es un asistente de voz creado con Python 3.12.4. Permite interactuar a través de comandos de voz para obtener información sobre temperatura, humedad y más, así como ejecutar diferentes funcionalidades. Además, cuenta con dos modos de ejecución: uno desde consola y otro como bot de Discord, conectándose a un canal de voz para responder a comandos de texto.

## Características

- **Comandos de voz (modo consola)**: 
  - **"oye roberto"**: Inicia la interacción con el asistente.
  - **"ayuda" o "opciones"**: Muestra las opciones disponibles, como consultar temperatura u humedad, ya sea del día actual o la media semanal, y la posibilidad de salir.
  - **"temperatura hoy"**: Indica la temperatura del día actual.
  - **"temperatura semana"**: Indica la temperatura media de la semana.
  - **"humedad hoy"**: Indica el porcentaje de humedad actual.
  - **"humedad semana"**: Muestra la humedad media de la semana.
  - **"ambas hoy"**: Muestra temperatura y humedad del día actual.
  - **"ambas semana"**: Muestra la temperatura y humedad medias de la semana.
  - **"salir"**: Finaliza la interacción.

- **Modo consola (main.py)**: Ejecutar `main.py` para iniciar el asistente de voz en consola.

- **Modo bot de Discord (discord_bot.py)**: Ejecutar `discord_bot.py` para lanzar el bot en Discord. Al escribir `!join` en el canal de texto, el bot se conectará al canal de voz y responderá con las mismas funcionalidades descritas anteriormente (temperatura, humedad, etc.).

## Requisitos Previos

- Python 3.12.4
- Archivo `requirements.txt` con las dependencias necesarias.

## Instalación

1. Clona el repositorio o descarga el código fuente.
2. Asegúrate de tener Python 3.12.4 instalado.
3. Instala las dependencias con:
   ```bash
   pip install -r requirements.txt



Thought about README en formato Markdown durante un segundo
md
Copiar código
# Asistente de Voz con Python

Este proyecto es un asistente de voz creado con Python 3.12.4. Permite interactuar a través de comandos de voz para obtener información sobre temperatura, humedad y más, así como ejecutar diferentes funcionalidades. Además, cuenta con dos modos de ejecución: uno desde consola y otro como bot de Discord, conectándose a un canal de voz para responder a comandos de texto.

## Características

- **Comandos de voz (modo consola)**: 
  - **"oye roberto"**: Inicia la interacción con el asistente.
  - **"ayuda" o "opciones"**: Muestra las opciones disponibles, como consultar temperatura u humedad, ya sea del día actual o la media semanal, y la posibilidad de salir.
  - **"temperatura hoy"**: Indica la temperatura del día actual.
  - **"temperatura semana"**: Indica la temperatura media de la semana.
  - **"humedad hoy"**: Indica el porcentaje de humedad actual.
  - **"humedad semana"**: Muestra la humedad media de la semana.
  - **"ambas hoy"**: Muestra temperatura y humedad del día actual.
  - **"ambas semana"**: Muestra la temperatura y humedad medias de la semana.
  - **"salir"**: Finaliza la interacción.

- **Modo consola (main.py)**: Ejecutar `main.py` para iniciar el asistente de voz en consola.

- **Modo bot de Discord (discord_bot.py)**: Ejecutar `discord_bot.py` para lanzar el bot en Discord. Al escribir `!join` en el canal de texto, el bot se conectará al canal de voz y responderá con las mismas funcionalidades descritas anteriormente (temperatura, humedad, etc.).

## Requisitos Previos

- Python 3.12.4
- Archivo `requirements.txt` con las dependencias necesarias.

## Instalación

1. Clona el repositorio o descarga el código fuente.
2. Asegúrate de tener Python 3.12.4 instalado.
3. Instala las dependencias con:
   ```bash
   pip install -r requirements.txt


## Configuración del Bot de Discord
Crea una aplicación y un bot desde el Portal de Desarrolladores de Discord.

Copia el token del bot.

Crea una carpeta config en la raíz del proyecto (si no existe).

Dentro de config, crea un archivo .env y añade la línea:

```bash
DISCORD_TOKEN=<TOKEN>
```

### Ejecución del Proyecto
Modo Consola:
Ejecuta:

```bash
python main.py
```

El asistente iniciará en modo consola.

### Modo Bot de Discord:
Ejecuta:

```bash
python discord_bot.py
```
Luego, desde tu servidor de Discord, escribe !join en un canal de texto y el bot se unirá a tu canal de voz, permitiendo las mismas consultas que el modo consola.