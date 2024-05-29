#!/bin/bash
#
########################################
#
# Nombre: 
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Simulador de banco con depósito a plazo fijo de interés compuesto.
# Entradas: euros_depo, porcent_tae, anhos_depo
# Salidas: 
#
########################################

euros_depo=$1
porcent_tae=$2
anhos_depo=$3

if [ -z "$1" ]; then
    echo "Error. No ha indicado la cantidad que desea ingresar."
    read -p "Indique cúanto desea ingresar en su cuenta: " euros_depo
elif [ -z "$2" ] then
    echo "Error. No ha indicado el %TAE."
    read -p "Indique el %TAE: " porcent_tae
elif [ -z "$3" ]; then
    echo "Error. No ha indicado durante cuántos años durará su depósito."
    read -p "Indique cuántos años durará su depósito: " anhos_depo
fi

echo "A continuación, se calculará el beneficio del que dispondrá dados los siguientes datos: "
echo "Dinero depositado: $euros_depo euros"
echo "Porcentaje de TAE: $por_tae"
echo "Duración de su depósito: $anhos_depo"

    for (( a=1; ia=$anhos_depo; a++ )) 
    do
        beneficio=$(echo "scale=2; $euros_depo * $por_tae / 100" | bc)
        total=$(echo "scale=2; $euros_depo + $beneficio" | bc)
        echo "Año $a: $euros_depo * (1 + $por_tae/100) = $total"
        echo "Enhorabuena, cuenta con un beneficio de $beneficio"
        euros_depo=$total
    done
fi
