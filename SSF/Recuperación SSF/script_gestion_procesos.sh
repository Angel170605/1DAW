#!/bin/bash
#
########################################
#
# Nombre: Script Gestión de Procesos
# Autor: Ángel Pérez <angelpd170605@gmail.com>
# Objetivo del script: Gestionar un paquete de software. Ofrecerá distintas opciones dependiendo de si el paquete está instalado o no.
# Entradas: maxCPU (Porcentaje máximo de uso de CPU), maxMem (Porcentaje máximo de uso de la memoria)
# Salidas: error100, error150, error200, Información del proceso, menús con opciones
#
########################################

if [ "$#" -ne 2 ]; then
echo "Error. Sólo se admietn 2 argumentos [maxCPU, MaxMem]. Por favor, indique los 2 argumentos en dicho orden."
exit 100

elif  [ "$2" -gt 100 ]; then
echo "Error. La capacidad maxCPU no puede ser superior a 100. Por favor, indique un valor entre 0 y 100."
exit 150

elif [ "$1" -lt 0 ] || [ "$0" -lt 0 ]; then
echo "Error. Ninguno de los valores requeridos puede ser inferior a 0. Por favor, indique valores iguales o superiores a 0"
exit 200

fi

maxCPU_actual=$(ps -eo %cpu --sort=-%cpu --no-headers | cut -d '.' -f 1 | head - 1)
maxMem_actual=$(ps -eo %mem --sort=-%mem --no-headers | cut -d '.' -f 1 )

CPU_PID=$(ps -eo pid --sort=-%cpu --no headers | head -1 )
Mem_PID=$(ps -eo pid --sort=-%mem --no-headers | head -1 )

while true; do
 
  # Si hay algún proceso que supere alguno de estos valores (si son los dos, elegir cualquiera de ellos), se mostrará información de dicho proceso y luego se imprimirá un menú para:

  if [ "$maxCPU_actual" -gt "$maxCPU"]; then
    echo "¡Cuidado! El proceso $CPU_PID está consumiendo más recursos de los que su CPU puede dar."

    echo "1. Ignorar el aviso y seguir comprobando"
    echo "2. Disminuir la prioridad del proceso"
    echo "3. Interrumpir el proceso"
    echo "4. Terminar el proceso"
    echo "5. Finalizar inmediatamente el proceso"
    echo "6. Detener el proceso (Congelación evitable)"
    echo "7. Detener el proceso (Congelación Inevitable)"
    reaqd -p "Por favor, seleccione el número de la medida que desee tomar: " opcion
  
    case "$option" in
      1) break;;
      2) nice -n -3 $CPU_PID;;
      3) kill -INT $CPU_PID;;
      4) kill -TERM $CPU_PID;;
      5) kill -KILL $CPU_PID;;
      6) kill -STOP $CPU_PID;;
      7) kill -TSP $CPU_PID;;

        esac
      done
    fi
  
  if [ "$maxMem_actual" -gt "$maxMem" ]; then
    echo "¡Cuidado! El proceso $Mem_PID está consumiendo más memoria de la tiene el sistema"

    echo "1. Ignorar el aviso y seguir comprobando"
    echo "2. Disminuir la prioridad del proceso"
    echo "3. Interrumpir el proceso"
    echo "4. Terminar el proceso"
    echo "5. Finalizar inmediatamente el proceso"
    echo "6. Detener el proceso (Congelación evitable)"
    echo "7. Detener el proceso (Congelación Inevitable)"
    reaqd -p "Por favor, seleccione el número de la medida que desee tomar: " opcion
  
    case "$option" in
      1) break;;
      2) nice -n -3 $Mem_PID;;
      3) kill -INT $Mem_PID;;
      4) kill -TERM $Mem_PID;;
      5) kill -KILL $Mem_PID;;
      6) kill -STOP $Mem_PID;;
      7) kill -TSP $Mem_PID;;

        esac
      done
    fi
done
  # Ignorar el aviso y seguir comprobando
  # Disminuir en 3 puntos la prioridad del proceso
  #  Interrumpir el proceso
  #  Terminar el proceso
  #  Finalizar inmediatamente el proceso
  #  Detener el proceso ("congelarlo" de forma evitable)
  #  Detener el proceso ("congelarlo" de forma INevitable)
  
  trap "echo 'Interrumpiendo ejecución'; exit 0" sigint
  trap "echo 'Finalizando ejecución'; exit 0" sigint
  trap "uptime" SIGUSR1
  trap "ulimit -a" SIGUSR2

  done
