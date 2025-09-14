import re
import time
import random
import csv


def leer_expresiones_regulares(ruta_archivo="expresiones_chatbot_hoteles.csv"):
    patrones = {}
    pesos = {}
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)  # saltar encabezado
        for intencion, patron, peso in lector:
            patron = patron.strip()
            patrones[intencion.strip()] = re.compile(patron, re.IGNORECASE)
            try:
                pesos[intencion.strip()] = int(peso.strip())
            except:
                pesos[intencion.strip()] = 1
    return patrones, pesos


def calcular_similitud(user_input, patrones, pesos):
    max_peso = 0
    intencion_detectada = None
    for intencion, patron in patrones.items():
        if patron.search(user_input):
            peso = pesos.get(intencion, 1)
            if peso > max_peso:
                max_peso = peso
                intencion_detectada = intencion
    return intencion_detectada, max_peso


def chatbot_hoteles(patrones, pesos):
    patron_saludo = patrones.get("saludo")
    patron_despedida = patrones.get("despedida")
    patron_salida = patrones.get("salida")
    patron_reservar = patrones.get("reservar")
    patron_cancelar = patrones.get("cancelar_reserva")
    patron_precio = patrones.get("precio")
    patron_servicios = patrones.get("servicios")
    patron_disponibilidad = patrones.get("accesibilidad")
    patron_ubicacion = patrones.get("ubicacion")
    patron_horarios = patrones.get("horarios")
    patron_transferencias = patrones.get("transferencias")
    patron_afirmacion = patrones.get("afirmacion")
    #agregar los patrones para mascotas
    patron_mascotas = patrones.get("mascotas")
    #agregar los patrones para accesibilidad
    patrones_accesibilidad = patrones.get("accesibilidad")
    patron_promociones = patrones.get("promocion")
    patron_tipo_habitacion_sencilla = patrones.get("tipo_habitacion_sencilla")
    patron_tipo_habitacion_doble = patrones.get("tipo_habitacion_doble")
    patron_tipo_habitacion_suite = patrones.get("tipo_habitacion_suite")

    contexto = {
        "correo": None,
        "telefono": None,
    }
    while True:
        time.sleep(1)
        user_input = input("Tú: ")

        intencion_detectada, max_peso = calcular_similitud(user_input, patrones, pesos)

        if not user_input.strip():
            print("Hoss: Por favor, ingresa un mensaje válido.")
            continue

        # Responde según la intención detectada
        if intencion_detectada == "salida" or intencion_detectada == "despedida":
            despedidas_respuestas = [
                "Hoss: ¡Adiós! Que tengas un excelente día.",
                "Hoss: ¡Hasta luego! No dudes en contactarme si necesitas ayuda.",
                "Hoss: ¡Fue un placer ayudarte! Que tengas un buen día.",
            ]
            print(random.choice(despedidas_respuestas))
            break
        elif intencion_detectada == "saludo":
            saludos_respuestas = [
                "Hoss: ¡Hola! soy Hoss ¿En qué puedo ayudarte hoy?",
                "Hoss: ¡Saludos! soy Hoss Estoy aquí para asistirte con tus necesidades de hotel.",
                "Hoss: ¡Hola! soy Hoss ¿Buscas reservar una habitación o necesitas información?",
            ]
            print(random.choice(saludos_respuestas))
            print("Puedes preguntarme sobre:")
            # Solamente ayudara a que se contacten con el usuario
            print("- Reservar una habitación")
            # Solamente ayudara a que se contacten con el usuario
            print("- Cancelar una reservación")
            # Dara informacion tanto de precios de habitaciones como de servicios, y promociones
            print("- Precios y tarifas")
            # Informacion sobre los servicios que ofrece el hotel
            print("- Servicios del hotel")
            # Informacion sobre la accesibilidad del hotel
            print("- Accesibilidad y discapacidades")
            # Informacion sobre la disponibilidad de habitaciones
            print("- Disponibilidad de habitaciones")
            # Informacion sobre la ubicacion del hotel (ficticio)
            print("- Ubicación y cómo llegar")
            # Informacion sobre los horarios de check-in y check-out
            print("- Horarios de check-in y check-out")
            # Informacion sobre las transferencias de pago
            print("- Transferencias de pago")
            continue
        elif intencion_detectada == "reservar":
            print("Hoss: Claro, puedo ayudarte a reservar una habitación.")
            print("¿Podrías proporcionarme tu correo electrónico?")
            user_input = input("Tú: ")
            if not user_input.strip():
                print("Hoss: Por favor, ingresa un mensaje válido.")
                continue
            patron = patrones.get("validar_correo")
            if not patron.search(user_input):
                print(
                    "Hoss: El correo electrónico proporcionado no es válido. Inténtalo de nuevo."
                )
                continue
            else:
                contexto["correo"] = user_input.strip()
                print(
                    "Hoss: Gracias. Ahora, por favor, proporciona tu número de teléfono."
                )
                user_input = input("Tú: ")
                if not user_input.strip():
                    print("Hoss: Por favor, ingresa un mensaje válido.")
                    continue
                patron = patrones.get("validar_telefono")
                if not patron.search(user_input):
                    print(
                        "Hoss: El número de teléfono proporcionado no es válido. Inténtalo de nuevo."
                    )
                    continue
                else:
                    contexto["telefono"] = user_input.strip()
                    print(
                        f"Hoss: Perfecto. He registrado tu correo ({contexto['correo']}) y teléfono ({contexto['telefono']}).\nNos contactaremos con usted para finalizar la reservación."
                    )
                    print("Hoss: ¿En qué más puedo ayudarte?")
                    continue
        elif intencion_detectada == "cancelar_reserva":
            print(
                "Hoss: Para cancelar una reservación, por favor contacta a nuestro equipo de soporte al cliente al correo soporte@hoteles.com"
            )
            continue
        elif intencion_detectada == "precio":
            respuestas = [
                "Hoss: Ofrecemos descuentos especiales para reservas anticipadas y estancias prolongadas. ¿Te gustaría saber más?",
                "Hoss: Los precios de las habitaciones comienzan desde $100 por noche. ¿Quieres información sobre algún tipo de habitación en particular?",
            ]
            print(random.choice(respuestas))
            user_input = input("Tú: ")
            if not user_input.strip():
                print("Hoss: Por favor, ingresa un mensaje válido.")
                continue
            patron = patrones.get("afirmacion")
            if patron.search(user_input):
                print(
                    "Hoss: Actualmente tenemos una promoción del 20% de descuento para reservas realizadas con al menos 30 días de anticipación."
                )
                print("Hoss: La habitación sencilla cuesta $100 por noche.")
                print("Hoss: La habitación doble cuesta $150 por noche.")
                print("Hoss: La suite cuesta $250 por noche.")
                print("Hoss: ¿En qué más puedo ayudarte?")
                continue
        elif intencion_detectada == "promocion":
            print(
                "Hoss: Actualmente tenemos una promoción del 20% de descuento para reservas realizadas con al menos 30 días de anticipación."
            )
            print("Hoss: ¿En qué más puedo ayudarte?")
            continue
        elif intencion_detectada == "tipo_habitacion_sencilla":
            print("Hoss: La habitación sencilla cuesta $100 por noche.")
            print("Hoss: ¿En qué más puedo ayudarte?")
            continue
        elif intencion_detectada == "tipo_habitacion_doble":
            print("Hoss: La habitación doble cuesta $150 por noche.")
            print("Hoss: ¿En qué más puedo ayudarte?")
            continue
        elif intencion_detectada == "tipo_habitacion_suite":
            print("Hoss: La suite cuesta $250 por noche.")
            print("Hoss: ¿En qué más puedo ayudarte?")
            continue
        elif intencion_detectada == "servicios":
            print(
                "Hoss: Nuestro hotel ofrece Wi-Fi gratuito, desayuno incluido, spa, gimnasio, piscina, restaurante bar, parking y servicio de habitaciones 24 horas."
            )
            print("Hoss: ¿En qué más puedo ayudarte?")
            continue
        elif intencion_detectada == "wifi":
            print(
                "Hoss: Sí, tenemos Wi-Fi gratuito en todo el hotel. De una velocidad de bajada de 20 Mbps y de subida de 10 Mbps."
            )
            print("Hoss: ¿En qué más puedo ayudarte?")
            continue
        elif intencion_detectada == "mascotas":
            print(
                "Hoss:Sí, puedes ingresar con mascotas o animales de servicio tales como perros lazarillo ó animlas de soporte emocianal."
                )
            print("Hoss: ¿En qué más puedo ayudarte?")        
            continue
        elif intencion_detectada == "accesibilidad":
            print(
                "Hoss: Sí, contamos con espacios accesibles para personas con capacidades diferentes."
                )
            print("Hoss: ¿En qué más puedo ayudarte?")
            continue
        elif intencion_detectada == "desayuno":
            print(
                "Hoss: Sí, el desayuno está incluido en la tarifa de la habitación y se sirve de 7:00 a 10:30 AM en el restaurante del hotel."
            )
            print("Hoss: ¿En qué más puedo ayudarte?")
            continue
        elif intencion_detectada == "spa":
            print(
                "Hoss: Sí, contamos con un spa que ofrece masajes, tratamientos faciales y corporales. Está abierto de 9:00 AM a 9:00 PM."
            )
            print("Hoss: ¿En qué más puedo ayudarte?")
            continue
        elif intencion_detectada == "gimnasio":
            print(
                "Hoss: Sí, contamos con un gimnasio equipado con máquinas de cardio y pesas. Está abierto las 24 horas."
            )
            print("Hoss: ¿En qué más puedo ayudarte?")
            continue
        elif intencion_detectada == "piscina":
            print(
                "Hoss: Sí, tenemos una piscina al aire libre disponible para nuestros huéspedes. Está abierta de 8:00 AM a 10:00 PM."
            )
            print("Hoss: ¿En qué más puedo ayudarte?")
            continue
        elif intencion_detectada == "ubicacion":
            print(
                "Hoss:Se encuentra en Calz. de Tlalpan 663, Álamos, Benito Juárez, 03400 Ciudad de México, CDMX"
                )
            print(
                "Hoss:Para llegar puedes llegar a metro xola y caminar en direccion al sur de la ciudad"
                )
            print("Hoss: ¿En qué más puedo ayudarte?")
            continue
        elif intencion_detectada == "restaurante_bar":
            print(
                "Hoss: Sí, contamos con un restaurante y bar que ofrece una variedad de platos y bebidas locales e internacionales. Está abierto de 12:00 PM a 11:00 PM."
            )
            print("Hoss: ¿En qué más puedo ayudarte?")
            continue
        elif intencion_detectada == "parking":
            print(
                "Hoss: Sí, ofrecemos estacionamiento gratuito para nuestros huéspedes. No es necesario reservar con anticipación."
            )
            print("Hoss: ¿En qué más puedo ayudarte?")
            continue
        elif intencion_detectada == "servicio_habitaciones":
            print(
                "Hoss: Sí, ofrecemos servicio de habitaciones las 24 horas. Puedes pedir desde el menú del restaurante directamente a tu habitación."
            )
            print("Hoss: ¿En qué más puedo ayudarte?")
            continue
        else:
            respuestas_default = [
                "Hoss: Lo siento, no entendí tu solicitud. ¿Podrías reformularla?",
                "Hoss: No estoy seguro de cómo ayudarte con eso. ¿Puedes darme más detalles?",
                "Hoss: No entiendo tu pregunta. ¿Podrías aclararla?",
            ]
            print(random.choice(respuestas_default))
            continue


if __name__ == "__main__":
    patrones, pesos = leer_expresiones_regulares()
    chatbot_hoteles(patrones, pesos)
