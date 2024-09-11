# Sistema de Biblioteca

## Actores

| Actor | Descripción |
| --- | --- |
| Usuario | Es una persona que puede acceder al catálogo de la biblioteca, buscar libros, reservarlos, prestarlos y devolverlos. |
| Bibliotecario | Es un empleado de la biblioteca que puede gestionar los libros, los usuarios y las reservas. |

## Casos de Uso

### Prestar Libro

| Caso de Uso | Prestar Libro |
| --- | --- |
| Objetivo | Permitir al usuario llevarse un libro de la biblioteca por un tiempo determinado. |
| Actores | Usuario, Bibliotecario |
| Precondiciones | El usuario debe estar registrado en el sistema y tener menos de tres libros prestados. El libro debe estar disponible en la biblioteca. |
| Flujo principal | 1. El usuario selecciona un libro del catálogo y lo lleva al mostrador. <br> 2. El bibliotecario escanea el código de barras del libro y del usuario. <br> 3. El sistema registra el préstamo y asigna una fecha de devolución. <br> 4. El bibliotecario entrega el libro al usuario y le informa de la fecha de devolución. <br> 5. El usuario recibe el libro y se va de la biblioteca. |
| Flujo alternativo | 3a. El sistema detecta que el libro está reservado por otro usuario. <br> 3a.1. El bibliotecario informa al usuario de que el libro no se puede prestar. <br> 3a.2. El usuario devuelve el libro al bibliotecario y puede elegir otro libro o salir de la biblioteca. |
| Postcondiciones | El usuario tiene el libro prestado y el sistema actualiza la disponibilidad del libro. |

### Devolver Libro

| Caso de Uso | Devolver Libro |
| --- | --- |
| Objetivo | Permitir al usuario devolver un libro que ha prestado de la biblioteca. |
| Actores | Usuario, Bibliotecario |
| Precondiciones | El usuario debe tener el libro prestado y estar dentro del plazo de devolución. |
| Flujo principal | 1. El usuario lleva el libro al mostrador. <br> 2. El bibliotecario escanea el código de barras del libro y del usuario. <br> 3. El sistema registra la devolución y actualiza la disponibilidad del libro. <br> 4. El bibliotecario confirma al usuario que ha devuelto el libro correctamente. <br> 5. El usuario se va de la biblioteca. |
| Flujo alternativo | 3a. El sistema detecta que el usuario ha excedido el plazo de devolución. <br> 3a.1. El bibliotecario informa al usuario de que tiene una multa por retraso. <br> 3a.2. El usuario paga la multa al bibliotecario. <br> 3a.3. El sistema registra el pago de la multa y actualiza la disponibilidad del libro. <br> 3a.4. El bibliotecario confirma al usuario que ha devuelto el libro y pagado la multa. <br> 3a.5. El usuario se va de la biblioteca. |
| Postcondiciones | El usuario ya no tiene el libro prestado y el sistema actualiza la disponibilidad del libro. |

### Buscar Libro

| Caso de Uso | Buscar Libro |
| --- | --- |
| Objetivo | Permitir al usuario consultar el catálogo de la biblioteca y encontrar libros de su interés. |
| Actores | Usuario |
| Precondiciones | El usuario debe estar registrado en el sistema y haber iniciado sesión. |
| Flujo principal | 1. El usuario accede a la función de búsqueda de libros. <br> 2. El sistema muestra una interfaz de búsqueda que permite al usuario ingresar términos de búsqueda, como título, autor o palabras clave. <br> 3. El usuario ingresa los términos de búsqueda y presiona "Buscar". <br> 4. El sistema realiza una búsqueda en la base de datos y muestra los resultados coincidentes. <br> 5. El usuario puede seleccionar un libro de la lista de resultados para obtener más información. |
| Flujo alternativo | 4a. El sistema no encuentra ningún libro que coincida con los términos de búsqueda. <br> 4a.1. El sistema muestra un mensaje de que no hay resultados. <br> 4a.2. El usuario puede modificar los términos de búsqueda y volver al paso 3 o salir de la función de búsqueda. |
| Postcondiciones | El usuario ha consultado el catálogo de la biblioteca y ha encontrado libros de su interés. |
