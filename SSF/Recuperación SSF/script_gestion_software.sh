#!/bin/bash
#
########################################
#
# Nombre: Script Gestión de Software
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Gestionar un paquete de software. Ofrecerá distintas opciones dependiendo de si el paquete está instalado o no.
# Entradas: Nombre de un paquete
# Salidas: Paquete instalado, Paquete no instalado, opciones [Mostrar versión del paquete/Reinstalarlo/Actualizarlo/Eliminarlo/Eliminarlo totalmente]
#
########################################

sudo apt-get update > /dev/null

paquete="$1"

while [ -z "$paquete" ]; do
    read -p "Introduzca el nombre del paquete: " paquete
done

mostar_informacion(){
 paquete="$1"
apt-cache show "$paquete"
}

instalar_paquete() {
paquete="$1"

	apt-get install "$paquete"
}

paquete_instalado() {
paquete="$1"
dpkg -l "$paquete" &> /dev/null
}

if paquete_instalado "$paquete"; then
    echo "El paquete $paquete está instalado."
    echo "1. Mostrar su versión"
    echo "2. Reinstalarlo"
    echo "3. Actualizarlo (si es actualizable)"
    echo "4. Eliminarlo (guardando la configuración)"
    echo "5. Eliminarlo totalmente"

    read -p "¿Qué quiere hacer con él?: " opcion

    case "$opcion" in
        1) mostrar_informacion "$paquete";;
        2) instalar_paquete "$paquete";;
        3) sudo apt upgrade "$paquete";;
        4) apt-get remove "$paquete";;
        5) apt-get purge "$paquete";;
        *) echo "Opción no disponible";;
    esac
else
    resultados=$(apt-cache search "$paquete")
    if [ -z "$resultados" ]; then
        echo "Lo siento, \"$paquete\" no se encuentra disponible en lso repositorios."
    else
        echo "Se han encontrados las siguientes coincidencias con $paquete: "
        echo "$resultados"
	read -p "¿Quiere instalar el paquete? [S/N]: " instalar
 	if [[ $instalar == "S" ]]; then
  	echo "De acuerdo. Iniciando la instalación de $paquete"
   	instalar_paquete "$paquete"
 
 	fi
 
   	if [[ $instalar != "N" ]]; then
    	echo "De acuerdo. $paquete no será instalado"
   	fi
    fi
fi
