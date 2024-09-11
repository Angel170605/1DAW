# Sistema de Reservas de Vuelos

## Actores

| Actor | Descripción |
| --- | --- |
| Pasajero | Es una persona que puede buscar, reservar y cancelar vuelos a través del sistema. |
| Agente de Reservas | Es un empleado de la aerolínea o de una agencia de viajes que puede gestionar las reservas de los pasajeros, modificar los datos de los vuelos y emitir los billetes. |

## Casos de Uso

### Buscar Vuelo

| Caso de Uso | Buscar Vuelo |
| --- | --- |
| Objetivo | Permitir al pasajero consultar la disponibilidad y el precio de los vuelos que se ajusten a sus preferencias. |
| Actores | Pasajero |
| Precondiciones | El pasajero debe estar registrado en el sistema y haber iniciado sesión. |
| Flujo principal | 1. El pasajero accede a la función de búsqueda de vuelos. <br> 2. El sistema muestra una interfaz de búsqueda que permite al pasajero ingresar los criterios de búsqueda, como origen, destino, fecha, número de pasajeros, clase, etc. <br> 3. El pasajero ingresa los criterios de búsqueda y presiona "Buscar". <br> 4. El sistema realiza una búsqueda en la base de datos y muestra los vuelos disponibles que coinciden con los criterios de búsqueda. <br> 5. El pasajero puede seleccionar un vuelo de la lista de resultados para obtener más información o reservarlo. |
| Flujo alternativo | 4a. El sistema no encuentra ningún vuelo que coincida con los criterios de búsqueda. <br> 4a.1. El sistema muestra un mensaje de que no hay vuelos disponibles. <br> 4a.2. El pasajero puede modificar los criterios de búsqueda y volver al paso 3 o salir de la función de búsqueda. |
| Postcondiciones | El pasajero ha consultado la disponibilidad y el precio de los vuelos que se ajustan a sus preferencias. |

### Reservar Vuelo

| Caso de Uso | Reservar Vuelo |
| --- | --- |
| Objetivo | Permitir al pasajero reservar un vuelo y obtener un código de reserva. |
| Actores | Pasajero, Agente de Reservas |
| Precondiciones | El pasajero debe haber seleccionado un vuelo
