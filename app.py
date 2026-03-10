from flask import Flask, render_template, request
import random

app = Flask(__name__)

OPCIONES = ["piedra", "papel", "tijera"]


def jugar_ronda(eleccion_usuario: str):
    eleccion_usuario = eleccion_usuario.lower()
    if eleccion_usuario not in OPCIONES:
        return None, None, "opcion_invalida"

    eleccion_pc = random.choice(OPCIONES)

    if eleccion_usuario == eleccion_pc:
        resultado = "empate"
    elif (
        (eleccion_usuario == "piedra" and eleccion_pc == "tijera")
        or (eleccion_usuario == "papel" and eleccion_pc == "piedra")
        or (eleccion_usuario == "tijera" and eleccion_pc == "papel")
    ):
        resultado = "ganaste"
    else:
        resultado = "perdiste"

    return eleccion_usuario, eleccion_pc, resultado


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    eleccion_usuario = None
    eleccion_pc = None
    error = None

    if request.method == "POST":
        eleccion_usuario = request.form.get("eleccion")
        eleccion_usuario, eleccion_pc, resultado = jugar_ronda(eleccion_usuario)
        if resultado == "opcion_invalida":
            error = "Opción no válida."
            resultado = None

    return render_template(
        "index.html",
        opciones=OPCIONES,
        resultado=resultado,
        eleccion_usuario=eleccion_usuario,
        eleccion_pc=eleccion_pc,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)

