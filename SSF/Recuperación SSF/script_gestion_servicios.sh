#!/bin/bash
#
########################################
#
# Nombre: Script Gestión de Servicios
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Gestionar un paquete de software. Ofrecerá distintas opciones dependiendo de si el paquete está instalado o no.
# Entradas: Nombre de un paquete
# Salidas: Paquete instalado, Paquete no instalado, opciones [Mostrar versión del paquete/Reinstalarlo/Actualizarlo/Eliminarlo/Eliminarlo totalmente]
#
########################################

servicio="$1"

while [ -z "$servicio" ]; do
  read -p "Por favor, indique el nombre del servicio a gestionar" servicio
done

systemctl status "$servivio" >/dev/null 2>/dev/null
if [ "$?" -eq 4 ]; then
    echo "Error. El servicio $servicio no se ha encontrado."
    exit 10
fi

if [ systemctl is-active $servicio == "active" ]; then
  echo "El servicio $servicio está activo."

elif [ systemctl is-active $servicio == "inactive" ]; then
  echo "El servicio $servicio está inactivo."

  fi

if [ systemctl is-enabled $servicio == "enabled" ]; then
  echo "El servicio $servicio está habilitado."

elif [ systemctl is-enabled $servicio == "disabled" ]; then
  echo "El servicio $servicio está deshabilitado"

elif [ systemctl is-enabled $servicio == "masked"]; then
  echo "El servicio $servicio está enmascarado"

  fi

echo "Tiene las siguientes opciones para la gestión del servicio"
echo "1. Activar/Descativar el servicio"
echo "2. Habilitar/Deshabilitar el servicio"
echo "3. Enmascarar/Desenmascarar el servicio"
echo "4. Mostrar la configuración del servicio"
echo "5. Reiniciar el servicio (Dejándolo activo)"
echo "6. Reiniciar el servicio (Dejándolo en su último estado)"
echo "7. Aplicar cambios en la configuración del servicio (Dejándolo en activo)"
echo "8. Aplicar cambios en la configuración del servicio (En su último estado)"
echo "9. Asignar la configuración de habilitado/deshabilitado indicada por el desarrollador"
echo "10. Mostrar el tiempo de carga total del sistema"
echo "11. Mostrar el nivel actual de ejecución del sistema"
echo "12. Apagar el equipo"
echo "13. Reiniciar el equipo"
echo "14. Salir"
read -p "Por favor, indique el número de la operación que desea realizar: " opcion

case $opcion in
1) if [ systemctl is-active $servicio == "active" ]; then
    sudo systemctl start $servicio
    elif [ systemctl is-active $servicio == "desactive" ]; then
    sudo systemctl stop $servicio
  fi ;;
  
2) if [ systemctl is-enabled $service == "enabled" ]; then
      sudo systemctl disable $servicio
      elif [ systemctl is-enabled $service == "disabled" ]; then
      sudo systemctl enable $service
    fi ;;
    
3) if [ systemctl is-enabled $servicio == "masked" ]; then
      sudo systemctl unmask $servicio
      else:
      sudo systemctl mask $servicio
    fi ;;
    
4) systemctl show $servicio ;;

5) sudo systemctl restart $servicio ;;

6) sudo systemctl try-restart $servicio ;;

7) sudo systemctl reload-or-restart $servicio ;;

8) sudo systemctl try-reload-or-restart $servicio ;;

9) systemd-analyze time ;;

10) echo "El tiempo de carga de $servicio es (systemd-analyze blame | grep "$svc_name" | tr -s " " | cut -d " " -f 2)" ;;

11) echo "El nivel de ejecucuión actual del sistema es " runlevel ;;

12) echo "Apagando el sistema..."
sleep 5
 sudo systemctl isolate runlevel0.target
 ;;

 13) echo "Reiniciando el sistema..."
 sudo systemctl isolate runlevel6.target
 ;;

 14) "¡Hasta la próxima!" 
 exit 0 ;;
 esac
done
