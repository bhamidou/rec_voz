from datetime import datetime, timedelta
from utils.read_file import ReadFile


class ReadClimate:
    def __init__(self, name_file):
        self.name_file = name_file
        self.file = ReadFile(self.name_file)
    
    def haveTempOrHumidity(self, arr):
        lineas = arr.splitlines()
        for linea in lineas:
            if 'humidity' in linea:
                return True, 'humidity'
            elif 'temperature' in linea:
                return True, 'temperature'
        return False, None
    
    def checkInWeek(self, fecha_str):
        hoy = datetime.now()
        lastWeek = hoy - timedelta(weeks=1)
        try:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%dT%H:%M:%S%z')
            fecha = fecha.replace(tzinfo=None)
        except ValueError:
            return False
        return lastWeek <= fecha <= hoy

    def getClima(self):
        arrClima = []
        arrTemp = []
        arrHumidity = []
        arr = self.file.getArr()

        i = len(arr) - 1
        fecha = arr[i].split(" ")[0]
        while self.checkInWeek(fecha) and i >=0:
            check, tipo = self.haveTempOrHumidity(arr[i])
            if(check):
                if(tipo=='temperature'):
                    arrTemp.append([fecha.split("T")[0], arr[i].split(" ")[3].split(":")[1].split("}")[0].split(",")[0]])
                else:
                    arrHumidity.append([fecha.split("T")[0], arr[i].split(" ")[3].split(":")[1].split("}")[0]])
            i -= 1
            fecha = arr[i].split(" ")[0]

        return arrTemp, arrHumidity
