#!/bin/bash
#
########################################
#
# Nombre: Calcula cambio
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Calcular el cambio que debe recibir un cliente, suponiendo que se contara con cambio ilimiado y hubieran billetes de 1 y 2 euros
# Entradas: precio_art, cant_pago
# Salidas: cant_cambio.
#
########################################

precio_art=$1
cambio_disp=(500 200 100 50 20 10 5 2 1)

if [ "$#" -ne 1 ]; then
    echo "Error. Debe indicar el valor del producto."
    exit
fi

read -p "Indique cuánto ha pagado por el artículo: " cant_pago

cambio=$((cant_pago - precio_art))

echo "Ha comprado un artículo con un precio de $precio_art, y ha pagado con $precio_art. Por tanto, el cambio es de: "

for c in "${cambio[@]}"
do
    billete=$((cambio / c))
    if [ "$billete" -gt 0 ]; then
        echo "$billete billete(s) de $c euro(s)"
        cambio=$((cambio - billete * c))
    fi
done
