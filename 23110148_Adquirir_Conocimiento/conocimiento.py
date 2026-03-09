import json
import os

ARCHIVO_CONOCIMIENTO = "conocimiento.json"


def cargar_conocimiento():
    if not os.path.exists(ARCHIVO_CONOCIMIENTO):
        return {}

    try:
        with open(ARCHIVO_CONOCIMIENTO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        print("Error: la base de conocimiento está corrupta.")
        return {}


def guardar_conocimiento(data):
    with open(ARCHIVO_CONOCIMIENTO, "w", encoding="utf-8") as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False)