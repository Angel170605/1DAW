#!/bin/bash
#
########################################
#
# Nombre: Password
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Pide una contraseña por teclado dos o más veces, hasta que coincida con la primera. Es como el clásico verificador de contraseñas que nos encontramos al crear cuentas, perfiles, etc.
# Entradas: contrasenha_original, verif_contrasenha
# Salidas: Mensaje variable.
#
########################################

read -s -p: "Introduzca la contraseña que desea utilizar: " contrasenha_original
read -s -p: "Vuelva a introducir la contraseña: " verif_contrasenha

if [ $contrasenha_original == $verif_contrasenha ]; then
  echo "Verificación completada. Su nueva contraseña es $contrasenha"
fi

while [ $contrasenha != $verif_contrasenha ] 
do 
  echo "Error de verificación. Las contraseñas no coinciden." 
  read -s -p "Por favor, inténtelo de nuevo: " verif_contrasenha
done
