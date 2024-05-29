#!/bin/bash
#
########################################
#
# Nombre: Calcula tiempos
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Pasar una cantidad determinada de segundos a dias/horas/minutos/segundos
# Entradas: total_segundos
# Salidas: dias, horas, minutos, segundos
#
########################################

if [ $# -nq 1 ]; then
    echo "Error. Debe indicar un único argumento. (Número de segundos)"

total_segundos=$1

dias=$((total_segundos/86400))
resto_segundos=$((total_segundos%86400))

horas=$((resto_segundos/3600))
resto_segundos=$((resto_segundos%3600))

minutos=$((resto_segundos/60))

segundos=$((resto_segundos%60))

echo "$total segundos son $dias dias, $horas horas, $minutos minutos y $segundos segundos."
