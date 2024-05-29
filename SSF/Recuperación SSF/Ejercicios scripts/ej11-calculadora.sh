#!/bin/bash
#
########################################
#
# Nombre: Calculadora
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Ofrece distintas operaciones con los valores de entrada.
# Entradas: num1, num2
# Salidas: Distintas operaciones
#
########################################

num1=$1
num2=$2

if [ -z $num1 ]; then
    read -p "Por favor, indique el primer valor con el que desea operar: " num1
fi
if [ -z $num2 ]; then
    read -p "Por favor, indique el segundo valor con el que desea operar: " num2
fi

echo "Puede seleccionar una de las siguientes operaciones: "
echo "1) Suma: Sumar $num1 y $num2"
echo "2) Resta: Restar $num1 y $num2"
echo "3) Multiplica: Multiplicar $num1 por $num2"
echo "4) Divide: Dividir $num1 entre $num2"
echo "5) Eleva: Eleva $num1 a $num2"
echo "6) Media: Calcula la media entre $num1 y $num2"
read -p "Por favor, indique el nombre o número de la operación que desee realizar: " opcion

case $opcion in
1 | "Suma" | "suma" )
echo "$num1 + $num2 = $((num1+num2))" ;;
2 | "Resta" | "resta" )
echo "$num1 - $num2 = $((num1-num2))" ;;
3 | "Multiplica" | "multiplica" )
echo "$num1 * $num2 = $((num1*num2))" ;;
4 | "Divide" | "divide" )
echo "$num1 / $num2 = $((num1/num2))" ;;
5 | "Eleva" | "eleva" )
echo "$num1 ^ $num2 = $((num1**num2))" ;;
6 | "Media" | "media" )
echo "La media entre $num1 y $num2 es $(((num1+num2)/2))" ;;
*) echo "Error. La opción $opcion no es válida."
