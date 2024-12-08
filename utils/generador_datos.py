import os
import random
from datetime import datetime, timedelta

# Nombre del archivo de salida
OUTPUT_FILE = "generated_shellyht.log"

# Formato para los tópicos y datos
TOPICS = [
    "online",
    "status/ble",
    "status/cloud",
    "status/devicepower:0",
    "status/ht_ui",
    "status/humidity:0",
    "status/mqtt",
    "status/sys",
    "status/temperature:0",
    "status/wifi",
    "status/ws",
    "events/rpc"
]

# Generar una línea de datos
def generate_line(timestamp):
    device_id = "shellyplusht-e86beae8c3d0"
    topic = random.choice(TOPICS)
    base_topic = f"{device_id}/{topic}"
    qos = 0
    retain = random.choice([0, 1])
    
    # Generación de payloads según el tópico
    payload = {}
    if topic == "online":
        payload = random.choice([True, False])
    elif topic == "status/cloud":
        payload = {"connected": random.choice([True, False])}
    elif topic == "status/devicepower:0":
        payload = {
            "id": 0,
            "battery": {"V": round(random.uniform(3.5, 6.0), 2), "percent": random.randint(0, 100)},
            "external": {"present": random.choice([True, False])}
        }
    elif topic == "status/humidity:0":
        payload = {"id": 0, "rh": round(random.uniform(30.0, 60.0), 1)}
    elif topic == "status/temperature:0":
        payload = {"id": 0, "tC": round(random.uniform(20.0, 30.0), 1), "tF": round(random.uniform(68.0, 86.0), 1)}
    elif topic == "status/sys":
        payload = {
            "mac": "E86BEAE8C3D0",
            "restart_required": False,
            "time": None,
            "unixtime": None,
            "uptime": random.randint(1, 100),
            "ram_size": 254088,
            "ram_free": random.randint(100000, 200000),
            "fs_size": 393216,
            "fs_free": random.randint(100000, 300000),
            "cfg_rev": 37,
            "reset_reason": random.randint(1, 10)
        }
    elif topic == "events/rpc":
        payload = {
            "src": device_id,
            "dst": f"{device_id}/events",
            "method": random.choice(["NotifyStatus", "NotifyFullStatus", "NotifyEvent"]),
            "params": {}
        }
    
    # String final
    payload_str = f'{{"tst":"{timestamp}","topic":"{base_topic}","qos":{qos},"retain":{retain},"payloadlen":{len(str(payload))},"payload":{payload}}}'
    return f'{timestamp} {base_topic} {payload} {payload_str}\n'

# Verificar si existen datos recientes
def check_existing_data():
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                last_date_str = last_line.split()[0]
                last_date = datetime.strptime(last_date_str, "%Y-%m-%dT%H:%M:%S%z")
                if datetime.now() - last_date < timedelta(days=7):
                    return True
    return False

# Generar datos
def generate_data():
    lines = []
    now = datetime.now()
    for i in range(100):  # Genera 100 líneas
        offset = random.choice([-1, 1]) * random.randint(0, 3600)
        timestamp = (now + timedelta(seconds=offset)).strftime("%Y-%m-%dT%H:%M:%S%z")
        lines.append(generate_line(timestamp))
    return lines

# Guardar datos
def save_data(lines):
    with open(OUTPUT_FILE, "a") as file:
        file.writelines(lines)

def main():
    if check_existing_data():
        print("Ya existen datos recientes. No se generan nuevos datos.")
    else:
        print("Generando nuevos datos...")
        lines = generate_data()
        save_data(lines)
        print(f"Datos generados y guardados en {OUTPUT_FILE}.")

if __name__ == "__main__":
    main()
