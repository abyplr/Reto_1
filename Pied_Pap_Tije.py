import random 
Jugador = input("Elige piedra, papel o tijeras: ")
Jugador = Jugador.lower() #Por si el usuario ingresa mayúsculas
#Se realiza para ver si la elección del usuario es válida (si no es asi, se le pide que ingrece una opción válida)
while True:
    if Jugador != 'piedra' and Jugador != 'papel' and Jugador != 'tijeras':
        Jugador = input("Elección inválida. Elige piedra, papel o tijeras: ")
        Jugador = Jugador.lower()
    else:
        break
#Para que la computarora elija aleatoriamente entre las tres opciones
computadora = random.choice(['piedra', 'papel', 'tijeras'])
print(f"La computadora eligió: {computadora}")
#Opciones de victoria, derrota o empate
if Jugador == 'piedra' and computadora == 'papel':
    print("Derrota")
elif Jugador == 'piedra' and computadora == 'tijeras':
    print("Victoria")
elif Jugador == 'papel' and computadora == 'tijeras':
    print("Derrota")
elif Jugador == 'papel' and computadora == 'piedra':
    print("Victoria")
elif Jugador == 'tijeras' and computadora == 'piedra':
    print("Derrota")
elif Jugador == 'tijeras' and computadora == 'papel':
    print("Victoria")
elif Jugador == computadora:
    print("Empate")