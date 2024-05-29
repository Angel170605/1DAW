#!/bin/bash
#
########################################
#
# Nombre: 
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Imprimir en pantalla un rectángulo cuyas dimensiones serán introducidas por el usuario.
# Entradas: base, altura (Hay valores por defecto)
# Salidas: Rectángulo de dimensiones variables.
#
########################################

base=7
altura=4
    
if [ "$#" -eq 1 ]; then
    base=$1
    altura=4
elif [ "s#"-eq 2 ]; then
    base=$1
    altura=$2
fi

area=$((base * altura))
for (( fila=1; fila<=altura; fila++ )); do
    for (( col=1; col<=base; col++ )); do
        echo -n "*"
    done
    echo
done

echo "El rectángulo tiene un área de $base X $altura, que equivale a $area"
