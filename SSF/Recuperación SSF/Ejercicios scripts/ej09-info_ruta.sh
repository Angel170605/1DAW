#!/bin/bash
#
########################################
#
# Nombre: Info ruta
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Se analiza el tipo del argumento de entrada (fichero, directorio, otros) para mostrar su información. 
# Entradas: arg
# Salidas: Información sobre el argumento
#
########################################

if [ "$#" -eq 0 ]; then
    echo "Error. Debe indicar un argumento."
    exit 
fi

arg=$1

if [ ! -e "$arg" ]; then
    echo "Error. No se ha encontrado la ruta $arg en el disco."
    exit 
fi

if [ -d "$arg" ]; then
    echo "$arg es un directorio"
elif [ -f "$arg" ]; then
    echo "$arg es un fichero"
elif [ -L "$arg" ]; then
    echo "$arg es un enlace"
else
    echo "$arg es un elemento distinto a un directorio, fichero o enlace"
fi


if [ -r "$arg" ] ; then
    echo "$arg tiene el permiso de lectura"
else
    echo "$arg no tiene el permiso de escritura"
fi

if [ -w "$arg" ]; then
    echo "$arg tiene el permiso de escritura"
else
    echo "$arg no tiene el permiso de escritura"
fi

if [ -x "$arg" ]; then
    echo "$arg tiene el permiso de ejecución"
else
    echo "$arg no tiene el permiso de ejecución"
fi


if [ -s "$arg" ]; then
    echo "$arg tiene contenido"
else
    echo "$arg está vacío"
fi
