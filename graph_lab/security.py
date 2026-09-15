from functools import wraps

from flask import (
    request,
    session,
    redirect,
    url_for
)


# =========================================================
# LIMITES
# =========================================================

MAX_INPUT_LENGTH = 100_000

MAX_DATA_POINTS = 10_000

MAX_FUNCTION_LENGTH = 200

MAX_TITLE_LENGTH = 100

MAX_AXIS_LENGTH = 50

MAX_ORBITAL_STEPS = 20_000


# =========================================================
# AUTENTICACIÓN
# =========================================================

def login_required(f):

    @wraps(f)
    def wrapper(*args, **kwargs):

        if not session.get("username"):

            return redirect(
                url_for("login")
            )

        return f(
            *args,
            **kwargs
        )

    return wrapper


# =========================================================
# LIMITAR TEXTO
# =========================================================

def validar_texto(
    valor,
    max_length,
    obligatorio=False
):

    if valor is None:

        valor = ""

    valor = str(valor).strip()

    if obligatorio and not valor:

        raise ValueError(
            "El campo es obligatorio."
        )

    if len(valor) > max_length:

        raise ValueError(
            f"El campo no puede superar "
            f"{max_length} caracteres."
        )

    return valor


# =========================================================
# VALIDAR LISTAS NUMÉRICAS
# =========================================================

def convertir_datos(
    texto,
    max_points=MAX_DATA_POINTS
):

    if texto is None:

        raise ValueError(
            "Debes introducir datos."
        )

    texto = str(texto).strip()

    if not texto:

        raise ValueError(
            "Debes introducir datos."
        )

    if len(texto) > MAX_INPUT_LENGTH:

        raise ValueError(
            "La entrada es demasiado grande."
        )

    valores = [
        valor.strip()
        for valor in texto.split(",")
        if valor.strip()
    ]

    if len(valores) > max_points:

        raise ValueError(
            f"El máximo permitido es "
            f"{max_points} puntos."
        )

    try:

        numeros = [
            float(valor)
            for valor in valores
        ]

    except ValueError:

        raise ValueError(
            "Todos los valores deben ser numéricos."
        )

    return numeros