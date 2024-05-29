#!/bin/bash
#
########################################
#
# Nombre: Resta
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Restar dos números.
# Entradas: num1, num2
# Salidas: result
#
########################################

if [ -z "$num1" ]; then
    echo "Error. Debe indicar dos valores."
    read -p "Por favor, indíque el primer valor: " num1
fi

if [ -z "$num2" ]; then
    echo "Error. Debe indicar dos valores."
    read -p "Por favor, indique el segundo valor: " num2
fi

num1=$1
num2=$2
result=$(($num1-$num2))

echo "El resultado de la operación $num1 - $num2 = $result"
