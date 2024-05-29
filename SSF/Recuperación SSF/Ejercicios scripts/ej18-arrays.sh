#!/bin/bash
#
########################################
#
# Nombre: Array
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Generará un array con los números recibidos, colocándolos al principio si so pares y al final si son impares.
# Entradas: números enteros
# Salidas: datos (array)
#
########################################

suma=0
datos=()
negativos=()

if [ "$#" -eq 0 ]; then
    echo "Error. Debe introducir, al menos, un valor."
    exit
fi

for n in "$@"
do
    if [ "$n" -lt 0 ]; then
        negativos+=("$n")
    else
        if [ "$((n % 2))" -eq 0 ]; then
            datos=("$n" "${datos[@]}") 
            echo "$n se inserta por el PRINCIPIO porque es PAR"
        elif [ "$((n%2))" -ne 0 ]; then
            datos+=("$n")
            echo "$n se inserta por el FINAL porque es IMPAR"
        fi
    fi
done

min=${datos[0]}
max=${datos[0]}

for n in "${datos[@]}" 
do
    if [ "$n" -lt "$min" ]; then
        min=$n
    elif [ "$n" -gt "$max" ]; then
        max=$n
    fi
done

for n in "${datos[@]}"; do
    suma=$((suma + n))
done

media=$((n / ${#datos[@]}))

echo "---"
echo "Array construido (${#datos[@]} elementos): ${datos[@]}"
echo "MIN: $min, MAX: $max, MEDIA: $media"
