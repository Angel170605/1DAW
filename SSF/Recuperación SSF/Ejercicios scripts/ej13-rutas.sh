#!/bin/bash
#
########################################
#
# Nombre: Rutas
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Ejectuta el script ej09-info_rutas.sh para cada elemento del directorio actual que tenga más de 4 carcateres.
# Entradas: Contenidos del directorio actual
# Salidas: Información de la ruta (Salida de ej09-info_ruta.sh)
#
########################################

contenido=$(find . -type d -name '????*')

for item in $contenido; 
do
    ./ej09-info_ruta.sh "$item"
done
