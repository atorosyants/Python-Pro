import random
import time

puntuacion = 0
numero1 = random.randint(1, 99)
numero2 = random.randint(1, 99)
operacion = random.randint(1, 4)

print("¡Hola!")
time.sleep(2)
print("Te voy a preguntar unas cuantas operaciones matemáticas.")
time.sleep(3)
print("Pero antes...")
time.sleep(2)

while True:
    querer = input("¿Aceptas el reto?")
    if querer == "Sí" or querer == "Si" or querer == "sí" or querer == "si":
        print("¡Muy bien!")
        time.sleep(2)
        print("¡Empecemos!")
        time.sleep(2)
        cantidad = int(input("¿Cuántas operaciones quieres resolver?"))
        print("¡Vale!")
        time.sleep(2)
        for i in range(cantidad):
            if operacion == 1:
                operacion = "+"
                problema1 = int(input("¿Cuánto es ", numero1, operacion + str(numero2) + "?"))
                if problema1 == numero1 + numero2:
                    puntuacion += 1
                    print("¡Muy bien!")
                    time.sleep(2)
                else:
                    print("¡Incorrecto!")
                    time.sleep(2)
                    print("La respuesta correcta es ", str(numero1 + numero2) + ".")
                    time.sleep(3.5)
            if operacion == 2:
                operacion = "-"
                problema2 = int(input("¿Cuánto es ", numero1, operacion + str(numero2) + "?"))
                if problema2 == numero1 + numero2:
                    puntuacion += 1
                    print("¡Excelente!")
                    time.sleep(2)
                else:
                    print("¡Mal!")
                    time.sleep(2)
                    print("La respuesta correcta es ", str(numero1 + numero2) + ".")
                    time.sleep(3.5)

            if operacion == 3:
                operacion = "*"
                problema3 = int(input("¿Cuántos es ", numero1, operacion + str(numero2) + "?"))
                if problema3 == numero1 + numero2:
                    puntuacion += 1
                    print("¡Listito!")
                    time.sleep(2)
                else:
                    print("¡Casi!")
                    time.sleep(2)
                    print("La respuesta correcta es ", str(numero1 + numero2) + ".")
                    time.sleep(3.5)
            
            
            if operacion == 4:
                operacion = "/"
                problema4 = int(input("¿Cuánto es ", numero1, operacion + str(numero2) + "?"))
                if problema4 == numero1 + numero2:
                    puntuacion += 1
                    print("¡Asombroso!")
                    time.sleep(2)
                else:
                    print("¡No tienes razón!")
                    time.sleep(2.5)
                    print("La respuesta correcta es ", numero1 + numero2 + ".")
                    time.sleep(3.5)

            print("Esas son todas las preguntas por hoy.")
            time.sleep(3)
            print("¡Pero, a lo mejor vuelvo con más!")
            time.sleep(3)
            print("Bueno...")
            time.sleep(2)
            print("¡Adiós!")
            time.sleep(2)
            print("Tu puntuación final ha sido " + str(puntuacion) + "/" + str(cantidad) + ".")
            break


    elif querer == "No" or querer == "no":
        print("¡Pues no pasa nada!")
        time.sleep(3)
        print("¡Otra vez será!")
        break
    else:
        print("No entendí lo que digiste...")
        time.sleep(3)