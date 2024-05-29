#!/bin/bash
#
########################################
#
# Nombre: Dia de la semana
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Calcular el día de la semana de una fecha determinada.
# Entradas: dia, mes, anho
# Salidas: dia_semana
#
########################################

if [ $# -ne 3 ]; then
    echo "Error. Debe indicar 3 valores."
    exit
fi

dia=$1
mes=$2
anho=$3

fecha="$anho-$mes-$dia"

dia_semana=$(date "$fecha" "+A%")

echo "El día de la semana de la fecha indicada ($dia/$mes/$anho) fue: $dia_semana"



