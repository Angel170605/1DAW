#!/bin/bash
#
########################################
#
# Nombre: Grados C2F
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Convierte el argumento de entrada (c: Temperatura en grados Celsius) a grados Fahrenheit con el uso de la fórmula " f = c * 1.8".
# Entradas: c (Temperatura en grados Celsius)
# Salidas: f (c convertida en grados Farenheit)
#
########################################

if [ $# -ne 1 ]; then
    echo "Error. Debe indicar una temperatura en grados Celsius."
    read -p "Por favor, indíquela a continuación: " c
fi

c=$1

f=$(echo "$c * 1.8 + 32" | bc)

echo "$c grados Celsius equivalen a $f grados Farenheit"

