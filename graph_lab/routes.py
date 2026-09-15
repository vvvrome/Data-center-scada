from flask import (
    Blueprint,
    render_template,
    request,
    session,
    redirect,
    url_for
)

import numpy as np
import matplotlib.pyplot as plt

from functools import wraps

from database.users import get_user_by_username
from database.audit import log_event
from .plotting import preparar_grafica
from .expression_parser import (
    evaluar_funcion,
    ExpressionSecurityError
)


# =========================================================
# BLUEPRINT
# =========================================================

graph_bp = Blueprint(
    "graph",
    __name__,
    url_prefix="/graph",
    template_folder="templates",
    static_folder="static"
)

@graph_bp.route("/")
def graph_index():

    return render_template(
        "graph_index.html"
    )
# =========================================================
# AUTENTICACIÓN
# =========================================================

def graph_login_required(f):

    @wraps(f)
    def wrapper(*args, **kwargs):

        username = session.get("username")

        if not username:
            return redirect(url_for("login"))

        user = get_user_by_username(username)

        if user is None:
            session.clear()
            return redirect(url_for("login"))

        return f(*args, **kwargs)

    return wrapper


# =========================================================
# AUDITORÍA
# =========================================================

def audit_graph(action, result, details=None):

    log_event(
        username=session.get("username", "UNKNOWN"),
        action=action,
        result=result,
        ip_address=request.remote_addr,
        user_agent=request.headers.get("User-Agent"),
        details=details
    )


# =========================================================
# DATOS
# =========================================================

@graph_bp.route("/datos", methods=["GET", "POST"])
@graph_login_required
def datos():

    grafica = None
    error = None

    if request.method == "POST":

        try:

            x_texto = request.form.get("x", "")
            y_texto = request.form.get("y", "")

            x = np.array([
                float(valor.strip())
                for valor in x_texto.split(",")
                if valor.strip()
            ])

            y = np.array([
                float(valor.strip())
                for valor in y_texto.split(",")
                if valor.strip()
            ])

            if x.size != y.size:
                raise ValueError(
                    "X e Y deben tener el mismo número de valores."
                )

            if x.size == 0:
                raise ValueError(
                    "Debes introducir datos."
                )

            titulo = request.form.get(
                "titulo",
                "Gráfica"
            )

            nombre_x = request.form.get(
                "nombre_x",
                "X"
            )

            nombre_y = request.form.get(
                "nombre_y",
                "Y"
            )

            fig, ax = preparar_grafica(
                figsize=(10, 6),
                titulo=titulo,
                xlabel=nombre_x,
                ylabel=nombre_y
            )

            ax.plot(
                x,
                y,
                marker="o",
                linewidth=2,
                label="Datos"
            )

            ax.legend()

            ruta = "API/static/grafica.png"

            fig.savefig(
                ruta,
                bbox_inches="tight",
                facecolor=fig.get_facecolor()
            )

            plt.close(fig)

            grafica = "grafica.png"

            audit_graph(
                "GRAPH_CREATED",
                "SUCCESS",
                f"Tipo=datos, puntos={x.size}"
            )

        except ValueError as e:

            error = str(e)

            audit_graph(
                "GRAPH_CREATED",
                "FAILED",
                error
            )

        except Exception as e:

            error = (
                "Ha ocurrido un error al generar la gráfica."
            )

            audit_graph(
                "GRAPH_CREATED",
                "ERROR",
                str(e)
            )

    return render_template(
        "datos.html",
        grafica=grafica,
        error=error
    )


# =========================================================
# TIPOS DE GRÁFICA
# =========================================================

@graph_bp.route("/tipos", methods=["GET", "POST"])
@graph_login_required
def tipos():

    grafica = None
    error = None

    if request.method == "POST":

        try:

            x_texto = request.form.get("x", "")
            y_texto = request.form.get("y", "")

            x = np.array([
                float(valor.strip())
                for valor in x_texto.split(",")
                if valor.strip()
            ])

            y = np.array([
                float(valor.strip())
                for valor in y_texto.split(",")
                if valor.strip()
            ])

            if x.size != y.size:
                raise ValueError(
                    "X e Y deben tener el mismo número de valores."
                )

            tipo = request.form.get(
                "tipo",
                "linea"
            )

            titulo = request.form.get(
                "titulo",
                "Gráfica"
            )

            nombre_x = request.form.get(
                "nombre_x",
                "X"
            )

            nombre_y = request.form.get(
                "nombre_y",
                "Y"
            )

            fig, ax = preparar_grafica(
                figsize=(10, 6),
                titulo=titulo,
                xlabel=nombre_x,
                ylabel=nombre_y
            )

            if tipo == "linea":

                ax.plot(
                    x,
                    y,
                    marker="o",
                    linewidth=2,
                    label="Datos"
                )

            elif tipo == "scatter":

                ax.scatter(
                    x,
                    y,
                    label="Datos"
                )

            elif tipo == "barras":

                ax.bar(
                    x,
                    y,
                    label="Datos"
                )

            else:

                raise ValueError(
                    "Tipo de gráfica no válido."
                )

            ax.legend()

            ruta = "API/static/grafica_tipos.png"

            fig.savefig(
                ruta,
                bbox_inches="tight",
                facecolor=fig.get_facecolor()
            )

            plt.close(fig)

            grafica = "grafica_tipos.png"
            ruta = "API/static/grafica_tipos.png"

            plt.savefig(
                ruta,
                bbox_inches="tight"
            )

            plt.close()

            grafica = "grafica_tipos.png"

            audit_graph(
                "GRAPH_CREATED",
                "SUCCESS",
                f"Tipo={tipo}, puntos={x.size}"
            )

        except ValueError as e:

            error = str(e)

            audit_graph(
                "GRAPH_CREATED",
                "FAILED",
                error
            )

        except Exception as e:

            error = (
                "Ha ocurrido un error al generar la gráfica."
            )

            audit_graph(
                "GRAPH_CREATED",
                "ERROR",
                str(e)
            )

    return render_template(
        "tipos.html",
        grafica=grafica,
        error=error
    )


# =========================================================
# FUNCIONES MATEMÁTICAS
# =========================================================

@graph_bp.route("/funciones", methods=["GET", "POST"])
@graph_login_required
def funciones():

    if request.method == "POST":

        try:

            funcion = request.form.get(
                "funcion",
                ""
            ).strip()

            inicio = float(
                request.form.get("inicio", "")
            )

            fin = float(
                request.form.get("fin", "")
            )

            puntos = int(
                request.form.get("puntos", "")
            )

        except (ValueError, TypeError):

            audit_graph(
                "INVALID_INPUT",
                "FAILED",
                "Datos inválidos en funciones"
            )

            return render_template(
                "funciones.html",
                error="Los datos introducidos no son válidos."
            )

        if not funcion:

            audit_graph(
                "INVALID_INPUT",
                "FAILED",
                "Función vacía"
            )

            return render_template(
                "funciones.html",
                error="Debes introducir una función."
            )

        if puntos < 2 or puntos > 100000:

            audit_graph(
                "INPUT_LIMIT_EXCEEDED",
                "BLOCKED",
                f"puntos={puntos}"
            )

            return render_template(
                "funciones.html",
                error=(
                    "El número de puntos debe estar "
                    "entre 2 y 100000."
                )
            )

        if inicio >= fin:

            return render_template(
                "funciones.html",
                error="El inicio debe ser menor que el final."
            )

        x = np.linspace(
            inicio,
            fin,
            puntos
        )

        try:

            y = evaluar_funcion(
                funcion,
                x
            )

            audit_graph(
                "FUNCTION_EVALUATED",
                "SUCCESS",
                f"function={funcion}, points={puntos}"
            )

        except ExpressionSecurityError as e:

            audit_graph(
                "FUNCTION_REJECTED",
                "BLOCKED",
                f"function={funcion}, reason={e}"
            )

            return render_template(
                "funciones.html",
                error=f"Expresión no permitida: {e}"
            )

        except Exception as e:

            audit_graph(
                "FUNCTION_ERROR",
                "ERROR",
                str(e)
            )

            return render_template(
                "funciones.html",
                error="No se ha podido calcular la función."
            )

        titulo = request.form.get(
            "titulo",
            f"f(x) = {funcion}"
        )

        nombre_x = request.form.get(
            "nombre_x",
            "X"
        )

        nombre_y = request.form.get(
            "nombre_y",
            "f(x)"
        )

        fig, ax = preparar_grafica(
            figsize=(10, 6),
            titulo=titulo,
            xlabel=nombre_x,
            ylabel=nombre_y
        )

        ax.plot(
            x,
            y,
            linewidth=2,
            label=funcion
        )

        ax.legend()

        fig.savefig(
            "API/static/grafica_funcion.png",
            bbox_inches="tight",
            facecolor=fig.get_facecolor()
        )

        plt.close(fig)

        return render_template(
            "funciones.html",
            grafica=True,
            funcion=funcion
        )

    return render_template(
        "funciones.html"
    )


# =========================================================
# VARIAS SERIES
# =========================================================

@graph_bp.route("/series", methods=["GET", "POST"])
@graph_login_required
def series():

    grafica = None
    error = None

    if request.method == "POST":

        try:

            numero_series = int(
                request.form.get(
                    "numero_series",
                    ""
                )
            )

            if numero_series < 1 or numero_series > 5:

                raise ValueError(
                    "El número de series debe estar entre 1 y 5."
                )

            titulo = request.form.get(
                "titulo",
                "Series"
            )

            nombre_x = request.form.get(
                "nombre_x",
                "X"
            )

            nombre_y = request.form.get(
                "nombre_y",
                "Y"
            )

            fig, ax = preparar_grafica(
                figsize=(10, 6),
                titulo=titulo,
                xlabel=nombre_x,
                ylabel=nombre_y
            )

            for i in range(
                1,
                numero_series + 1
            ):

                x_texto = request.form.get(
                    f"x{i}",
                    ""
                )

                y_texto = request.form.get(
                    f"y{i}",
                    ""
                )

                nombre = request.form.get(
                    f"nombre{i}",
                    f"Serie {i}"
                )

                x = np.array([
                    float(valor.strip())
                    for valor in x_texto.split(",")
                    if valor.strip()
                ])

                y = np.array([
                    float(valor.strip())
                    for valor in y_texto.split(",")
                    if valor.strip()
                ])

                if x.size != y.size:

                    raise ValueError(
                        f"La serie {i} tiene diferente "
                        "cantidad de valores X e Y."
                    )

                ax.plot(
                    x,
                    y,
                    marker="o",
                    linewidth=2,
                    label=nombre
                )

                fig.savefig(
                    "API/static/grafica_series.png",
                    bbox_inches="tight",
                    facecolor=fig.get_facecolor()
                )

                plt.close(fig)

            grafica = "grafica_series.png"

            audit_graph(
                "GRAPH_CREATED",
                "SUCCESS",
                f"Tipo=series, series={numero_series}"
            )

        except ValueError as e:

            error = str(e)

        except Exception as e:

            error = (
                "No se ha podido generar la gráfica."
            )

            audit_graph(
                "GRAPH_CREATED",
                "ERROR",
                str(e)
            )

    return render_template(
        "series.html",
        grafica=grafica,
        error=error
    )


# =========================================================
# ANÁLISIS
# =========================================================

@graph_bp.route("/analisis", methods=["GET", "POST"])
@graph_login_required
def analisis():

    grafica = None
    error = None
    resultado = {}

    if request.method == "POST":

        try:

            x_texto = request.form.get(
                "x",
                ""
            )

            y_texto = request.form.get(
                "y",
                ""
            )

            x = np.array([
                float(valor.strip())
                for valor in x_texto.split(",")
                if valor.strip()
            ])

            y = np.array([
                float(valor.strip())
                for valor in y_texto.split(",")
                if valor.strip()
            ])

            if x.size != y.size:

                raise ValueError(
                    "X e Y deben tener el mismo número de valores."
                )

            if x.size < 2:

                raise ValueError(
                    "Se necesitan al menos 2 puntos."
                )

            derivada = np.gradient(
                y,
                x
            )

            integral = np.trapezoid(
                y,
                x
            )

            indice_max = np.argmax(y)
            indice_min = np.argmin(y)

            media = np.mean(y)
            desviacion = np.std(y)

            resultado = {
                "integral": integral,
                "max_x": x[indice_max],
                "max_y": y[indice_max],
                "min_x": x[indice_min],
                "min_y": y[indice_min],
                "media": media,
                "desviacion": desviacion
            }

            fig, ax = preparar_grafica(
                figsize=(10, 6),
                titulo="Análisis de datos",
                xlabel="X",
                ylabel="Y"
            )

            plt.plot(
                x,
                y,
                marker="o",
                label="Datos"
            )

            ax.plot(
                x,
                y,
                marker="o",
                linewidth=2,
                label="Datos"
            )

            ax.axhline(
                0,
                linewidth=0.8
            )

            fig.savefig(
                "API/static/grafica_analisis.png",
                bbox_inches="tight",
                facecolor=fig.get_facecolor()
            )

            plt.close(fig)

            grafica = "grafica_analisis.png"

            audit_graph(
                "DATA_ANALYSIS",
                "SUCCESS",
                f"puntos={x.size}"
            )

        except ValueError as e:

            error = str(e)

        except Exception as e:

            error = (
                f"Error durante el análisis: {e}"
            )

    return render_template(
        "analisis.html",
        grafica=grafica,
        error=error,
        resultado=resultado
    )


# =========================================================
# ÓRBITA
# =========================================================

@graph_bp.route("/orbital", methods=["GET", "POST"])
@graph_login_required
def orbital():

    error = None
    trayectoria = None
    resultados = None

    if request.method == "POST":

        try:

            G = float(request.form["G"])
            M = float(request.form["M"])
            m = float(request.form["m"])

            x = float(request.form["x"])
            y = float(request.form["y"])
            z = float(request.form["z"])

            vx = float(request.form["vx"])
            vy = float(request.form["vy"])
            vz = float(request.form["vz"])

            dt = float(request.form["dt"])
            pasos = int(request.form["pasos"])

            if G <= 0:
                raise ValueError(
                    "G debe ser mayor que 0."
                )

            if M <= 0:
                raise ValueError(
                    "La masa central debe ser mayor que 0."
                )

            if m <= 0:
                raise ValueError(
                    "La masa del planeta debe ser mayor que 0."
                )

            if dt <= 0:
                raise ValueError(
                    "dt debe ser mayor que 0."
                )

            if pasos < 1:
                raise ValueError(
                    "Los pasos deben ser mayores que 0."
                )

            if pasos > 100000:
                raise ValueError(
                    "El máximo es de 100000 pasos."
                )

            posiciones_x = []
            posiciones_y = []
            posiciones_z = []

            velocidad_x = []
            velocidad_y = []
            velocidad_z = []

            velocidades = []
            distancias = []

            energia_cinetica = []
            energia_potencial = []
            energia_total = []

            for i in range(pasos):

                r = np.sqrt(
                    x**2 +
                    y**2 +
                    z**2
                )

                if r == 0:

                    raise ValueError(
                        "El planeta no puede estar en el centro."
                    )

                ax = -G * M * x / r**3
                ay = -G * M * y / r**3
                az = -G * M * z / r**3

                vx = vx + ax * dt
                vy = vy + ay * dt
                vz = vz + az * dt

                x = x + vx * dt
                y = y + vy * dt
                z = z + vz * dt

                posiciones_x.append(x)
                posiciones_y.append(y)
                posiciones_z.append(z)

                velocidad_x.append(vx)
                velocidad_y.append(vy)
                velocidad_z.append(vz)

                velocidad = np.sqrt(
                    vx**2 +
                    vy**2 +
                    vz**2
                )

                velocidades.append(
                    velocidad
                )

                distancias.append(r)

                Ec = 0.5 * m * velocidad**2
                Ep = -G * M * m / r
                Et = Ec + Ep

                energia_cinetica.append(Ec)
                energia_potencial.append(Ep)
                energia_total.append(Et)

            posiciones_x = np.array(posiciones_x)
            posiciones_y = np.array(posiciones_y)
            posiciones_z = np.array(posiciones_z)

            velocidad_x = np.array(velocidad_x)
            velocidad_y = np.array(velocidad_y)
            velocidad_z = np.array(velocidad_z)

            velocidades = np.array(
                velocidades
            )

            distancias = np.array(
                distancias
            )

            energia_cinetica = np.array(
                energia_cinetica
            )

            energia_potencial = np.array(
                energia_potencial
            )

            energia_total = np.array(
                energia_total
            )

            trayectoria = {
                "x": posiciones_x.tolist(),
                "y": posiciones_y.tolist(),
                "z": posiciones_z.tolist(),
                "vx": velocidad_x.tolist(),
                "vy": velocidad_y.tolist(),
                "vz": velocidad_z.tolist()
            }

            resultados = {
                "distancia_final": float(
                    distancias[-1]
                ),

                "velocidad_final": float(
                    velocidades[-1]
                ),

                "energia_cinetica": float(
                    energia_cinetica[-1]
                ),

                "energia_potencial": float(
                    energia_potencial[-1]
                ),

                "energia_total": float(
                    energia_total[-1]
                )
            }

            audit_graph(
                "ORBITAL_SIMULATION",
                "SUCCESS",
                f"steps={pasos}"
            )

        except ValueError as e:

            error = str(e)

        except Exception as e:

            error = (
                f"Error durante la simulación: {e}"
            )

            audit_graph(
                "ORBITAL_SIMULATION",
                "ERROR",
                str(e)
            )

    return render_template(
        "orbital.html",
        trayectoria=trayectoria,
        resultados=resultados,
        error=error
    )