#!/bin/bash
#
########################################
#
# Nombre: Multiplo
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Comprobar si los valores que recibe el script son múltiplos de otro número.
# Entradas: numeros de entrada, num
# Salidas: Verificación de múltiplos
#
########################################

if [ "$#" -eq 0 ]; then
    echo "Error. Debe introducir, al menos, un valor."
    exit 
fi

read -p "Introduzca un valor: " num

for n in $@
do  
    if [ "$((num%$valor))" -eq 0 ]; then
        echo "El número $num es múltiplo de $valor"
    else
        echo "El número $num no es múltiplo de $valor"
    fi
done
