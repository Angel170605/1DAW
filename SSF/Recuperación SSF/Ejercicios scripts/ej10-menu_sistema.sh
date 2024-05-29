#!/bin/bash
#
########################################
#
# Nombre: Menu sistema
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Ofrece distintas opciones relacionadas con el sistema.
# Entradas: nombre/número de la opción
# Salidas: Operación seleccionada
#
########################################

echo "Dispone de las siguientes opciones"

echo "1) porlibre: Indica el porcentaje de espacio libre de la partición raíz."
echo "2) tamlibre: Indica el tamaño del espacio libre de la partición raíz."
echo "3) usuario: Indica el usuario actual."
echo "4) maquina: Indica el nombre de la máquina."
echo "5) usuarios: Indica el número de usuarios del sistema."
echo "6) espacio: Total de espacio usado en todos mis directorios personales (en formato "humano": M, G, ...)"
echo "7) directorio: Mostrar el directorio actual"
echo "8) salir: Salir"
read -p "Introduzca el nombre o número de la opción que desee ejecutar: " opcion

case "$opcion" in
    "porlibre" | 1)
        echo "El porcentaje de espacio libre de la partición raíz $(df -h | cut -f5)" ;;
    "tamlibre" | 2)
         echo "La partición raiz tiene $(df -h | cut -f3) de espacio libre" ;;
    "usuario" | 3) 
        echo " El nombre del usuario actual es $(whoami)" ;;
    "maquina" | 4) 
        echo "El nombre de la máquina actual es $(hostname)" ;;
    "usuarios" | 5)  
        echo "La máquina tiene $(who | cut -d " " -f 1 | sort -u | wc -l) usuarios" ;;
    "espacio" | 6)
        echo "Hay un total de $(du -sh /home/* | cut -f1) usados en directorios personales" ;;
    "permisos" | 7)
        echo "Actualmente e¡se encuentra en el directorio $(pwd) " ;;
    "salir" | 8)
        echo "A continuación se saldrá del menú"
        exit ;;
    *)  echo "Error. La opción '$opcion' no es válida." ;;
