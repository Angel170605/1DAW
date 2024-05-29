#!/bin/bash
#
########################################
#
# Nombre: Pares
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Mostrar el cuadrado de los números pares que se encuentren en el rango entre los dos números especificados (num1, num2).
# Entradas: num1, num2
# Salidas: números
#
########################################

num1=$1
num2=$2

while [ -z "$num1" ] || [ -z "$num2" ]
do
    read -p "Error. No ha introuducido el primer valor. Pro favor, indíquelo: " num1
    read -p "Error. No ha introducido el segundo valor. Por favor, indíquelo: " num2
done

if [ "$num1" -gt "$num2" ]; then
    $num3v=$num1
    num1=$num2
    num2=$num3
fi

for num in $(seq $num1 $num2)
do
  if [ $((num%2)) -eq 0 ]; then
    echo "El cuadrado de $num es $((num * num))"
  fi
done
