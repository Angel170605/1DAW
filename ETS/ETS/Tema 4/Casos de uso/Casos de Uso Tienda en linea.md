# Sistema de Gestión de Tienda en Línea

## Actores

| Actor | Descripción |
| --- | --- |
| Cliente | Es una persona que puede ver el catálogo de productos, realizar compras, consultar el estado de sus pedidos y contactar con el servicio de atención al cliente. |
| Administrador | Es un empleado de la tienda en línea que puede gestionar el catálogo de productos, el inventario, los pedidos, los pagos, las devoluciones y el servicio de atención al cliente. |

## Casos de Uso

### Ver Catálogo

| Caso de Uso | Ver Catálogo |
| --- | --- |
| Objetivo | Permitir al cliente ver los productos disponibles en la tienda en línea y filtrarlos por categorías, precios, valoraciones, etc. |
| Actores | Cliente |
| Precondiciones | El cliente debe estar registrado en el sistema y haber iniciado sesión. |
| Flujo principal | 1. El cliente accede a la función de ver catálogo. <br> 2. El sistema muestra una interfaz de catálogo que permite al cliente ver los productos disponibles y filtrarlos por diferentes criterios. <br> 3. El cliente puede seleccionar un producto para ver más detalles o añadirlo al carrito de compras. |
| Flujo alternativo | 2a. El sistema detecta que no hay productos disponibles en el catálogo. <br> 2a.1. El sistema muestra un mensaje de que no hay productos disponibles. <br> 2a.2. El cliente puede salir de la función de ver catálogo. |
| Postcondiciones | El cliente ha visto los productos disponibles en la tienda en línea y ha podido filtrarlos por sus preferencias. |

### Realizar Compra

| Caso de Uso | Realizar Compra |
| --- | --- |
| Objetivo | Permitir al cliente comprar los productos que ha añadido al carrito de compras y obtener un código de pedido. |
| Actores | Cliente, Administrador |
| Precondiciones | El cliente debe tener al menos un producto en el carrito de compras. |
| Flujo principal | 1. El cliente accede a la función de realizar compra. <br> 2. El sistema muestra una interfaz de compra que permite al cliente revisar los productos en el carrito de compras, modificar las cantidades o eliminar productos. <br> 3. El cliente presiona "Continuar" en la interfaz de compra. <br> 4. El sistema muestra una interfaz de envío que permite al cliente ingresar o seleccionar su dirección de envío y elegir el método de envío. <br> 5. El cliente ingresa o selecciona su dirección de envío y elige el método de envío. <br> 6. El cliente presiona "Continuar" en la interfaz de envío. <br> 7. El sistema muestra una interfaz de pago que permite al cliente ingresar o seleccionar su método de pago y confirmar el importe total de la compra. <br> 8. El cliente ingresa o selecciona su método de pago y confirma el importe total de la compra. <br> 9. El sistema valida el método de pago.
