"""
✨ Escribe un decorador que permita "debugear" una función.

El decorador llamado "debug" deberá mostrar por pantalla (print):
- El nombre de la función decorada.
- Los argumentos posicionales.
- Los argumentos nominales.
- El resultado de la función decorada.

Ejemplo: Para la función "avg" definida en este fichero,
la salida debería ser:

func=<function avg at 0x10449d080>
args=(4, 3, 9, 7, 2, 8)
kwargs={}
result=5.5

💡 Haz uso del modo "debug" de los f-strings para mostrar
el valor de las variables:
https://aprendepython.es/core/datatypes/strings/#modo-debug
"""


def debug(avg):
    def wrapped(*args, **kwargs):
        result = avg(*args, **kwargs)
        func = avg
        return print(f'{func=} {args=} {kwargs=} {result=}', end=' ')

    return wrapped


@debug
def avg(*values: int) -> float:
    return sum(values) / len(values)


avg(4, 3, 9, 7, 2, 8)
