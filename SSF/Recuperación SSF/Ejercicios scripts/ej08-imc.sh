#!/bin/bash
#
########################################
#
# Nombre: IMC
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Calcula el IMC (Índice de masa corporal) del usuario e indica su estado vital en base a los resultados.
# Entradas: altura (cm), peso (kg)
# Salidas: IMC, diagnostico
#
########################################

altura=$1
peso=$2

IMC=$(echo "$peso * 1000 / ($altura * $altura)" | bc)
echo "Tu IMC (Índice de masa corporal) es $IMC"

if ((IMC < 16 )); then
    diagnostico="Delgadez severa"
elif ((IMC >= 16.99 ));
    diagnostico="Delgadez moderada"
elif ((IMC <= 18.49)); then
    diagnostico="Delgadez leve"
elif ((IMC <= 24.99)); then
    diagnostico="Peso normal"
elif ((IMC <= 29.99)); then
    diagnostico="Sobrepeso"
elif ((IMC <= 34.99)); then
    diagnostico="Obesidad leve"
elif ((IMC <= 39.99)); then
    diagnostico="Obesidad media"
else
    diagnostico="Obesidad severa"
fi

echo "Según tu IMC ($IMC), el resultado de tu diagnóstico es: $diagnostico"

