import random

opciones = ["piedra", "papel", "tijera"]

print("=== Juego: Piedra, Papel o Tijera ===")

while True:
    eleccion_usuario = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").strip().lower()

    if eleccion_usuario == "salir":
        print("Gracias por jugar. ¡Hasta luego!")
        break

    if eleccion_usuario not in opciones:
        print("Opción no válida. Intenta de nuevo.\n")
        continue

    eleccion_pc = random.choice(opciones)
    print(f"La computadora eligió: {eleccion_pc}")

    if eleccion_usuario == eleccion_pc:
        print("Empate.\n")
    elif (
        (eleccion_usuario == "piedra" and eleccion_pc == "tijera") or
        (eleccion_usuario == "papel" and eleccion_pc == "piedra") or
        (eleccion_usuario == "tijera" and eleccion_pc == "papel")
    ):
        print("¡Ganaste!\n")
    else:
        print("Perdiste.\n")