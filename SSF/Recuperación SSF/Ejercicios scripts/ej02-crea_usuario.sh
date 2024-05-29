#!/bin/bash
#
########################################
#
# Nombre: Crea usuario.
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Imprimmir un menasje en pantalla.
# Entradas: nombre, apellidos, usuario.
# Salidas: Mensaje con los datos del usuario.
#
########################################

if [ $# -lt 3 ]; then
    echo "Error. Debe indicar, al menos, tres argumentos [nombre, apellidos, usuario]."
    exit
fi

nombre=$1
apellidos=$2
usuario=$3

echo "Bienvenido, $nombre"
echo "Tus datos son: $nombre $apellidos"
echo "Vamos a crear tu usuario: $usuario"
echo "Tu nueva ID es $RANDOM"
