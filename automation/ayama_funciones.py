def validar_edad_halcon(edad):
    if 1 <= edad <= 30:
        return True
    else:
        return False

def evaluar_señal(funcion_obtener_señal):
    señal = funcion_obtener_señal()
    if señal == 0:
        return "Señal perdida"
    return "Señal OK"

import requests

def obtener_estado_servidor():
    respuesta = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return respuesta
    return respuesta
    return respuesta