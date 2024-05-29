#!/bin/bash
#
########################################
#
# Nombre: Calculadora func
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Realizar las operaciones de "ej11-calculadora.sh", pero con funciones.
# Entradas: num1, num2
# Salidas: result
#
########################################

suma() {
    echo "$num1 + $num2 = $((num1+num2))"
}
resta() {
    echo "$num1 - $num2 = $((num1-num2))"
}
multiplicacion() {
    echo "$num1 * $num2 = $((num1*num2))"
}
division() {
    echo "$num1 / $num2 = $((num1/num2))"
}
elevar() {
  echo "$num1 ^ $num2 = $((num1**num2))"
}
media() {
  echo "La media entre $num1 y $num2 es $(((num1+num2)/2))"
}
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
1 | "Suma" | "suma" ) suma ;;
2 | "Resta" | "resta" ) resta ;;
3 | "Multiplica" | "multiplica" ) multiplicacion ;;
4 | "Divide" | "divide" ) division ;;
5 | "Eleva" | "eleva" ) elevar ;;
6 | "Media" | "media" ) media ;;
*) echo "Error. La opción $opcion no es válida."
