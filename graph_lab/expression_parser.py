import ast
import numpy as np


# Funciones matemáticas que permitimos utilizar
FUNCIONES_PERMITIDAS = {
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "sqrt": np.sqrt,
    "exp": np.exp,
    "log": np.log,
    "abs": np.abs
}


# Constantes matemáticas permitidas
CONSTANTES_PERMITIDAS = {
    "pi": np.pi,
    "e": np.e
}


# Excepción específica para errores de seguridad
class ExpressionSecurityError(Exception):
    pass


def evaluar_funcion(expresion, x):
    """
    Evalúa una expresión matemática de forma segura.

    Ejemplos permitidos:
        x
        x + 2
        x**2
        2*x
        sin(x)
        cos(x)
        exp(-x)
        sqrt(x)
        log(x)
        pi*x

    Ejemplos rechazados:
        import os
        open(...)
        __import__(...)
        exec(...)
        x.attr
        x[0]
        lambda x: x
    """

    # ---------------------------------------------------------
    # 1. Comprobar que la expresión sea una cadena
    # ---------------------------------------------------------

    if not isinstance(expresion, str):
        raise ExpressionSecurityError(
            "La expresión debe ser texto."
        )

    expresion = expresion.strip()

    # ---------------------------------------------------------
    # 2. Limitar longitud
    # ---------------------------------------------------------

    if len(expresion) == 0:
        raise ExpressionSecurityError(
            "La expresión está vacía."
        )

    if len(expresion) > 200:
        raise ExpressionSecurityError(
            "La expresión es demasiado larga."
        )

    # ---------------------------------------------------------
    # 3. Parsear la expresión como expresión matemática
    # ---------------------------------------------------------

    try:
        arbol = ast.parse(expresion, mode="eval")
    except SyntaxError:
        raise ExpressionSecurityError(
            "La expresión matemática no es válida."
        )

    # ---------------------------------------------------------
    # 4. Evaluar el árbol de forma segura
    # ---------------------------------------------------------

    resultado = _evaluar_nodo(arbol.body, x)

    return resultado


def _evaluar_nodo(nodo, x):

    # ---------------------------------------------------------
    # Números
    # ---------------------------------------------------------

    if isinstance(nodo, ast.Constant):

        # No permitimos booleanos
        if isinstance(nodo.value, bool):
            raise ExpressionSecurityError(
                "Los valores booleanos no están permitidos."
            )

        # Solo permitimos números
        if not isinstance(nodo.value, (int, float)):
            raise ExpressionSecurityError(
                "Solo se permiten valores numéricos."
            )

        # Evitar infinitos y NaN introducidos como constantes
        if not np.isfinite(nodo.value):
            raise ExpressionSecurityError(
                "El valor numérico no es válido."
            )

        return nodo.value

    # ---------------------------------------------------------
    # Variable x
    # ---------------------------------------------------------

    if isinstance(nodo, ast.Name):

        if nodo.id == "x":
            return x

        if nodo.id in CONSTANTES_PERMITIDAS:
            return CONSTANTES_PERMITIDAS[nodo.id]

        raise ExpressionSecurityError(
            f"El identificador '{nodo.id}' no está permitido."
        )

    # ---------------------------------------------------------
    # Operaciones matemáticas
    # ---------------------------------------------------------

    if isinstance(nodo, ast.BinOp):

        izquierda = _evaluar_nodo(nodo.left, x)
        derecha = _evaluar_nodo(nodo.right, x)

        # Suma
        if isinstance(nodo.op, ast.Add):
            return izquierda + derecha

        # Resta
        if isinstance(nodo.op, ast.Sub):
            return izquierda - derecha

        # Multiplicación
        if isinstance(nodo.op, ast.Mult):
            return izquierda * derecha

        # División
        if isinstance(nodo.op, ast.Div):
            return izquierda / derecha

        # Módulo
        if isinstance(nodo.op, ast.Mod):
            return izquierda % derecha

        # Potencia
        if isinstance(nodo.op, ast.Pow):

            # Para evitar exponentes arbitrariamente grandes,
            # solo permitimos exponentes numéricos constantes.
            if not isinstance(nodo.right, ast.Constant):
                raise ExpressionSecurityError(
                    "El exponente debe ser un número constante."
                )

            exponente = nodo.right.value

            if not isinstance(exponente, (int, float)):
                raise ExpressionSecurityError(
                    "El exponente debe ser numérico."
                )

            if abs(exponente) > 20:
                raise ExpressionSecurityError(
                    "El exponente máximo permitido es 20."
                )

            return izquierda ** exponente

        raise ExpressionSecurityError(
            "Esta operación matemática no está permitida."
        )

    # ---------------------------------------------------------
    # Operaciones unarias: -x y +x
    # ---------------------------------------------------------

    if isinstance(nodo, ast.UnaryOp):

        valor = _evaluar_nodo(nodo.operand, x)

        if isinstance(nodo.op, ast.USub):
            return -valor

        if isinstance(nodo.op, ast.UAdd):
            return +valor

        raise ExpressionSecurityError(
            "Esta operación unaria no está permitida."
        )

    # ---------------------------------------------------------
    # Funciones matemáticas
    # ---------------------------------------------------------

    if isinstance(nodo, ast.Call):

        # Solo permitimos llamadas a nombres simples:
        # sin(x)
        # cos(x)
        #
        # No permitimos:
        # np.sin(x)
        # objeto.funcion(x)

        if not isinstance(nodo.func, ast.Name):
            raise ExpressionSecurityError(
                "Solo se permiten funciones matemáticas autorizadas."
            )

        nombre_funcion = nodo.func.id

        if nombre_funcion not in FUNCIONES_PERMITIDAS:
            raise ExpressionSecurityError(
                f"La función '{nombre_funcion}' no está permitida."
            )

        # Solo un argumento
        if len(nodo.args) != 1:
            raise ExpressionSecurityError(
                "Las funciones deben recibir exactamente un argumento."
            )

        # No permitimos argumentos con nombre
        if nodo.keywords:
            raise ExpressionSecurityError(
                "No se permiten argumentos con nombre."
            )

        argumento = _evaluar_nodo(nodo.args[0], x)

        funcion = FUNCIONES_PERMITIDAS[nombre_funcion]

        return funcion(argumento)

    # ---------------------------------------------------------
    # Cualquier otro tipo de nodo queda bloqueado
    # ---------------------------------------------------------

    raise ExpressionSecurityError(
        f"Elemento no permitido: {type(nodo).__name__}"
    )