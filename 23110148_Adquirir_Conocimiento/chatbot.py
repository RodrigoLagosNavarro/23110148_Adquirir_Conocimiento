import difflib
from conocimiento import cargar_conocimiento, guardar_conocimiento


def buscar_respuesta(pregunta, conocimiento):

    pregunta = pregunta.lower()

    # buscar coincidencia cercana
    coincidencias = difflib.get_close_matches(
        pregunta,
        conocimiento.keys(),
        n=1,
        cutoff=0.6
    )

    if coincidencias:
        return conocimiento[coincidencias[0]]

    return None


def chat():

    conocimiento = cargar_conocimiento()

    print("Chatbot iniciado.")
    print("Escribe 'salir' para terminar.\n")

    while True:

        usuario = input("Tú: ").lower()

        if usuario == "salir":
            print("Chatbot: Hasta luego.")
            break

        respuesta = buscar_respuesta(usuario, conocimiento)

        if respuesta:
            print("Chatbot:", respuesta)

        else:
            print("Chatbot: No conozco la respuesta.")

            nueva_respuesta = input(
                "¿Qué debería responder cuando me pregunten eso?: "
            )

            conocimiento[usuario] = nueva_respuesta
            guardar_conocimiento(conocimiento)

            print("Chatbot: Gracias, he aprendido algo nuevo.")

if __name__ == "__main__":
    chat()