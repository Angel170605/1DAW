#!/bin/bash
#
########################################
#
# Nombre: Compara
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Compara dos números, indicando cúal es mayor o si son iguales
# Entradas: num1, num2
# Salidas: result
#
########################################

num1=$1
num2=$2
if [ -z "$num1" ]; then
    read -p "Por favor, introduzca el primer valor a comparar: " num1
fi

if [ -z "$num2" ]; then
    read -p "Por favor, indique el segundo valor a comparar: " num2
fi

if [ "$num1" -gt "$num2" ]; then
    echo "$num1 es mayor que $num2"
elif [ "$num1" -lt "$num2" ]; then
    echo "$num1 es menor que $num2"
else
    echo "$num1 es igual que $num2"
fi
    
