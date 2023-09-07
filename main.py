import re
import tkinter as tk

# Set de respuestas y variables
aux: int = 0
respuestas = {
    "hola": "¡Que onda viejillo! ¿Pa que soy bueno?",
    "recomiendame unas rolitas": "Va,viejon, ¿Como te sientes pa.?",
    "": "No entiendo tu pregunta. Por favor, intenta de nuevo.",
}

respuestas_dolidas = {
    "dolido": "¿En que nivel de dolido viejo del  1 al 5?",
    "1": "Pa estos caso no andas tan sad : No cap (Junior H) ",
    "2": "Y viejo esos casi algo, si duelen un chingo : abecdario (Junior H) ",
    "3": "No hay pedo pa, hay mas culos que estrellas : El patrocinador (Junior H) ",
    "4": "Que chinge a su madre la culera: Dias Nublados (Junior H) ",
    "5": "Ella no te merecia pa,eres mucha carne para ese chihuahua : Album:Sad Boyz 4 life (Junior H) ",
    "otra": "Va,viejon, ¿Como te sientes pa.?",
    "": "No entiendo tu pregunta. Por favor, intenta de nuevo."

}
respuestas_belicas = {
    "belico": "¿Que tan belico anda viejo del 1 al 5?",
    "1": "Apenas empezando?  : Paris (Junior H) ",
    "2": "Ajala ya esta haciendo efecto el periquin : Cuerno Mio (Junior H) ",
    "3": "Ya se va a prender el ambiente : El Azul (Junior H) ",
    "4": "Ya se prendio ua,ua,ua,Primooo bajese:  El Tsurito (Junior H) ",
    "5": "Ya anda bien avionado pa,Cuidado : Lady Gaga (Junior H) ",
    "otra": "Va,viejon, ¿Como te sientes pa.?",
    "": "No entiendo tu pregunta. Por favor, intenta de nuevo."
}

respuestas_Enamoradas = {
    "belico": "¿Que tan belico anda viejo del 1 al 5?",
    "1": "Si te contesto el mensaje despues de la peda   : Ella (Junior H) ",
    "2": "aaa,viejo ya anda quedando la primera cita : Psicodelica (Junior H) ",
    "3": "aaa, ya primera cita : fin de semana (Junior H) ",
    "4": "te le vas a declarar verdad, hay te va pura inspiracion : Naci para Amarte  (Junior H) ",
    "5": "Ya son novios di : Loco Enamorado (Junior H) ",
    "otra": "Va,viejon, ¿Como te sientes pa.?",
    "": "No entiendo tu pregunta. Por favor, intenta de nuevo."
}


# Función para obtener la respuesta del chatbot
def obtener_respuesta():
    global aux
    mensaje_usuario = entrada.get()
    cadena_limpia = re.sub(r"[^a-zA-Z0-9\s]", '', mensaje_usuario.lower())
    if cadena_limpia == "belico":
        aux = 2
    elif cadena_limpia == "dolido":
        aux = 1
    elif cadena_limpia == "enamorado":
        aux = 3
    respuesta = chatbot_responder(cadena_limpia, aux)
    conversacion.config(state=tk.NORMAL)
    conversacion.insert(tk.END, f"Usuario: {mensaje_usuario}\n")
    conversacion.insert(tk.END, f"Chatbot: {respuesta}\n\n")
    conversacion.config(state=tk.DISABLED)
    entrada.delete(0, tk.END)


# Funcion que verifica el estado de ánimo y da una respuesta segun este
def chatbot_responder(mensaje_usuario, band):
    if band == 1 and mensaje_usuario in respuestas_dolidas:
        return respuestas_dolidas[mensaje_usuario]

    elif band == 2 and mensaje_usuario in respuestas_belicas:
        return respuestas_belicas[mensaje_usuario]

    elif band == 3 and mensaje_usuario in respuestas_Enamoradas:
        return respuestas_Enamoradas[mensaje_usuario]

    elif mensaje_usuario in respuestas:
        return respuestas[mensaje_usuario]
    else:
        return respuestas[""]


if __name__ == "__main__":
    # Configurar la ventana principal
    ventana = tk.Tk()
    ventana.title("Recomendador de rolitas Junior H")

    # Crear un campo de texto para el título
    titulo = tk.Label(ventana, text="Recomendador de rolitas Junior H(segun esta de animo)", font=("Roboto", 12),
                      pady=9, fg="grey")
    titulo.pack()

    # Crear un widget de conversación
    conversacion = tk.Text(ventana, wrap=tk.WORD, fg="red", )
    conversacion.pack(padx=10, pady=10)
    conversacion.config(state=tk.DISABLED)
    # Crear un widget de entrada de texto
    entrada = tk.Entry(ventana, width=70, justify="center")
    entrada.pack(padx=10, pady=10)

    # Crear un botón para enviar mensajes
    boton_enviar = tk.Button(ventana, text="Enviar", command=obtener_respuesta, fg="blue")
    boton_enviar.pack(padx=10, pady=10)

    ventana.mainloop()
