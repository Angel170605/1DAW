<div align = "center">
  
# REDES

<img src = "https://www.orbit.es/wp-content/uploads/2019/09/redes-cloud.jpg">


</div>

## CONTENIDOS

[1. Conexiones](#conexiones)

[2. Capas OSI](#capasosi)

[3. Clasificación de redes](#clasificacionderedes)

> [3.1 Capa Física](#capafisica)

> [3.2 Enlace DE DATOS](#enlacededatos)

> [3.3 Red](#capadered)

[4. Topología de la red](#topologiadelared)

[5. Canal/Ondas](#ondas)

[6. Cables](#cables)

[Comandos](#comandos)

[Definiciones](#definiciones)


## 1. CONEXIONES <a name="conexiones"></a>

### ¿Cómo viajan las conexiones?

1. Transductor de entrada

> 

2. Emisor

3. CANAL

4. Receptor
  
5. Transductor de salida

</div>

### Tipos de conexiones:

Guiada (Alámbrica):
  
> Eléctrico
  
> Óptico

> Par Trenzado 
    
No guiada (Inalámbrica)

> Bluethoot

> Wifi

> [Ondas](#ondas)

## 2. CAPAS OSI <a name="capasosi"></a>

### Características:

- 7 capas independientes

- Clasistas/Racistas/Machistas/Xenófobas ( Sólo hablan con sus iguales )

### Capas:

### 1. Capa física <a name="capafisica"></a>

#### Gran aportación: Envío de mensajes

Cacharros: Hub | Repetidores | ONT | Modem (señal a )

Recibe los datos y los pasa a la capa superior

### 2. Enlace de Datos <a name="enlacededatos"></a>

#### Gran aportación: Dirección MAC

Cacharros: Switch, Bridge, AP (Bridge muy especial)

- 2 Subcapas:

    - LLC -> Recibe el mensaje y lo manda directamente al que lo debe recibir
    
    - MAC ( Middle Control Acces ) -> Evita que haya colisiones
  
  - Dominio de colisión -> Son los segmentos en los que todos sus dispositivos pueden chocar entre sí
  
  - Nodos -> Dispositivos de acceso a la red

  - Trama -> Es el nombre que reciben los datos tratados en esta capa

  - Entramado -> Es la información añadida al  mensaje original (Destinatario y otras cosas)

  - Unicast -> Envía el mensaje dispositivo a dispositivo
  
  - BROADCAST -> Enviar mensaje a todos los dispositivos

  - Multicast -> Envia el mensaje a algunos si y otros no
 
  - Switch -> Une la **misma** red.
 
  - Router -> Une las **distintas** redes. ( Pertenece a la Capa 3: Red )
 
  - IFG -> Interframe Gap


### 3. Red <a name="capadered"></a>

#### Gran aportación: IP

Cacharros: Router (Realmente realmente, capa 3/4) | Firewall (Realmente realmente, capa 3/4)

> Intentará mediante todos los medios que el mensaje llegue a la siguiente capa; busca el mejor camino a través de la Red.

  IP: 

  - Estáticas o dinámicas (Lo decide el que la configure)

  - Públicas o privadas

  - 4 dígitos

  - NO hay núemros negativos

  - Cuantos mas equipos hayan, mayor será la red; de tal forma que se irán nombrando como S1, S2, S3... en un orden de mayor a menor.

  - Los números que la componen NO pueden superar el 255

  - Protocolo Apipa ( Automatic Private Internet Protocol Addressing ): Cuando no podemos obtener una IP válida, nos inventamos una dentro de un rango específico. No funcionará a nivel interno; pero sí a nivel externo.
    
  - Compuesta por:
  
      - Red
   
      - Host
   
    #### Clases:
  
      - Clase A: 0 - 127
    
      - Clase B: 128 - 191 
 
      - Clase C: 192 - 224
 
      - Experimentales ( Reservadas para el futuro | Restringidas, no se la puedes asignar a un equipo ):
 
        - Clase D: 224 - 239
     
        - Clase E: 240 - 255
 
- Se separa la Red del Host según la clase [ A | B | C | D ]
 
      ```
      EJEMPLO:
  
       A  B  C  D

      177.100.18.05 -> Clase B -> | RED: 177.100 | HOST: 18.05 |

      119.18.45.0 -> Clase A -> | RED: 119 | HOST: 18.45.0 |

      160.220.024.12 -> Clase B -> | RED: 160 | HOST: 220.024.12 |
      ```
- Para saber si es pública o privada:

    ```
    La IP privadas empiezan por 10, 172 o 192; aunque pueden existir IPs públicas que empiecen tanto por 172 como por 192
    ```

- Máscaras de Red:

  ```
  EJEMPLO  

  Clase A: 121.31.53.8
    Máscara: 255.0.0.0
  
  Clase B: 172.24.108.3
    Máscara 255.255.0.0  

  Clase C: 192.168.4.20
    Máscara: 255.255.255.0

  ```

- CIDR (Class-less Inter Domain Routing) 

> Número de 1 consecutivos que tiene una máscara de capa

  ```
  EJEMPLO  

  Clase A: 121.31.53.8
    Máscara: 255.0.0.0
      CIDR: /8

  Clase B: 172.24.108.3
    Máscara 255.255.0.0  
      CIDR: /16

  Clase C: 192.168.4.20
    Máscara: 255.255.255.0
      CIDR: /24

  El corte estará en el bit nº CIDR, en el número convertido a binario.
  ```

#### EJERCICIO DE REDES OFICINA ( EJERCICIO 12, CAE EN EL EXAMEN ): 

- Se identifican los routers ( R1, R2, R3...)

- También se identifican las redes ( Unidas por routers).

    - Es en sentido horario, de forma que se nombrarán ( eth0, eth1, eth2...etc) primero hacia arriba, luego hacia la izqd, abajo y drch.
 
    - La conexión entre los routers e Internet se llama ppp0 ( Aunque no sea común, pueden haber más: ppp1, ppp2, ppp3...etc)
 
    -   Nombres de las subredes: Nombre del router + Nombre de la red -> **R**n**eth**n.
 
      ```
      EJEMPLO
                  PC3 ( 30 redes )          PC2 ( 15 redes)            Servidores
                          |                        |                       |  
                          |                        | eth2                  | eth0
                          |                        |                       |
                      [ SWIFT ] - - - eth4 - - - ( R2 ) - - - eth1 - - - ( R1 ) 
                          |                        |                       |
                          |                        | eth3                  | ppp0
                          |                        |                       |
                  PC4 ( 20 redes)           PC2 ( 40 redes )           Internet
      ```

    - Campos diagrama IP:

      - VERS: Versión del protocolo IP usado para crear el datagrama.
      - HLEN: Longitud del Header.
      - Tipo de Servicio:
            - Prioridad (3 bits): Va desde 0 (*Baja prioridad*) hasta 7 (*Alta prioridad*)
            - Bit D (*Delay*)
            - Bit T ()
            - Bit R ()
      - Longitud Total
      - Identificación: Nº de secuencia, dirección de origen y destino, y protocolo usado
      - Banderas
      - Desesplazamientos de fragmentación
      - Tiempo de vida
      - Protocolo
      - CRC () Cabecera: Contiene la suma de los cálculos de la comprobación de errores de la cabecera del datagrama.
      - Dirección de Origen
      - Dirección de destino
      - Opciones IP: No es obligatorio y especifica las opciones solicitadas por el usuario que realiza el envío
      - Relleno
      - Datos

### 4. Transporte

#### Gran aportación: Puertos

Cacharros: ª

> Supervisa que los mensajes lleguen a la capa de red, y si no lo hacen, los solicita de nuevo | "Corta" el paquete en pequeños paquetitos, que luego serán juntados de nuevo en el paquete por la capa Transporte del destino.

- Podemos usar muchas apps y cosas con un sólo cable.

- Segmentación: Trocea y manda los archivos en cachitos cuyo tamaño es el MTU (Máximo tamaño que soporta la capa inferior)

- Reensanblamiento de segmentos.

- Puertos:

  -  Hay 2¹⁶ puertos (65535).
 
  -  Puerto 80 'por defecto':

      - Más fácil acceso: Normalmente suelen buscar este
   
      - Al igual que en términos de acceso, suele ser el primero al que intentan atacar.
   
  - Protocolo más importante: TCP:
 
      - Desventaja: Sólo enviará a la aplicación los datos que sean exactamente igual a los que envió origen. ¿Que le falta un bit? nada; a casa socio. Son los códigos de la red, es lo que hay.

  - Protocolo UTCP: (Tenso)
 

  Puertos exóticos:

    - 789: Puerto que usa Epoptes
    - 443: Conexiones encriptadas
    - 

### 5. Sesión

> Verifica que el destino está activo/en linea

Cacharros: No hay :(

### 6. Presentación

> Codifica los mensajes, se encarga de ver en qué formato van los archivos, el lenguaje de codificación (UTF-8, etc.), etc.

Cacharros: No hay :(

### 7. Aplicación

Cacharros: Servidores (Manejan información y contenido) | Proxy (Intermediario que rompe la conexión directa y da el anonimato)

Protocolos:

- Funciones:
    - Servidor web

- Servidores:
  - DNS TCP/UDP -> | Puertor: 53 |
  - Telnet -> 80
  - E-mail -> | Puertos: Jamón |
  - DHCP (Dynamic Host Configuration Protocol) -> UDP | Puertos: 67 servidor | 68 clientes
  - Web: https -> 443
  - FTP (File Transport Protocol): Servidores exclusivos para descargar -> | Puertos: 20 | 21
  - SMTP (Simple Mail Transfer Protocol) -> | Puertos: 25 mensajes sin cifrar | 587 mensajes cifrados.
 

- PARTES DE LA URL:

    https -> esquema

    udc.com -> Dominio
                        
    433 -> Puerto (No se suele poner)

    principal/historia -> ruta

    tumbalo=mich -> parametros

    \# hola -> "índice"

## 3. CLASIFICACIÓN DE REDES <a name="clasificacionderedes"></a>

### ¿Para qué? Para saber cómo montarlas, organizarlas, etc.

 **W** ( Wireless [ Puede estar o no ] ) + **X** ( Letra de clasificación ) + **AN** ( Area Network )

- BAN (Body)

- CAN:

  -  Campos

  -  Controller

- HAN (Home)

- LAN (Local)

- MAN (Metropolitan)

- NAN (Near me)

- PAN (Personal)

- SAN (Storage)

- WAN (Wide)

## 4. TOPOLOGÍA DE LA RED <a name = "topologiadelared"></a> :

### 4.1 TOPOLOGÍA FÍSICA:

- #### MODELO BUS

- #### MODELO ANILLO

  - ##### ANILLO SIMPLE
 
  - #### DOBLE ANILLO
 
- #### TIPO ESTRELLA ( SE USA AHORA )

- #### TIPO ÁRBOL

- #### TIPO MALLA

<div align = "center">

<img src="https://i.ytimg.com/vi/N26ocF-x9lo/hqdefault.jpg">

</div>

### 4.2 TOPOLOGÍA LÓGICA:

Es el sistema operativo el que se debe adaptar a los protocolos de la red, dado que estos están diseñados de forma que son iguales en todo el mundo.

## 5. CANAL / ONDAS <a name="ondas"></a>

### 5.1 Posibles complicaciones:

1. Ruido

 ```
   Están clasificados por colores, muy similar al espectro, siendo el ruido rosa el más agudo y el marrón el más grave.
```

  > Para solucionarlo, el ruido que queremos emitir debe ser más fuerte que el que se genera.

2. Atenuación

 ```
La señal va perdiendo intensidad
```

3. Distorción

### 5.2 Modulaciones:

1. AM

```
Cambiar la amplitud (Tamaño de la ola)
```

2. FM

```
Cambiar la freceuncia
```

3. PM

```
"Cambiar si sube o baja"
```

## 6. CABLES <a name=cables></a>

1. UTP [Unshielded Twisted Pair]

> 

2. STP [Shielded Twisted Pair]

> 

3. FTP [Foiled Twisted Pair]

> Enpantallamiento global

### Categorías

3. 10 Mbits/seg. Se usa para telefonía de voz, 10Base-T Ethernet, Token Ring a 4 Mbits/seg.

4. 16 Mbits/seg. Token Ring a 16 Mbits/seg.

5. ª 

===============================================================================================

Ventajas fibra óptica:

- Alcance

- Inmunidad a las interferencias

Tipos de fibra óptica:

<div align = "center">

<img src="https://acf.geeknetic.es/imgw/imagenes/tutoriales/57-3.jpg?f=webp" height="50%" width="50%">

</div>

## COMANDOS <a name=comandos></a>

## Linux:

- ifconfig: Ver dirección de red, y más información.

- ping: muestra información sobre una red, como la IP

- route: Ver las tablas de ruteo bien exóticas.

- route -n: Mide con métricas bien insanotas.

- traceroute: Permite ver por dónde pasan los paquetes y modificarlos. Lo usan generalmente los administradores.
  
- traceroute [dirección url (www.holasoyunejemplo.com)]: Muestra todos los saltos necesarios para llegar a la url especificada.

- netstat: Ver rutas de red y cosas exóticas

## Windows:

- ipconfig: Ver dirección de red, y más información.

## DEFINICIONES <a name=definiciones></a>
  
TCP/IP --> "une" Internet (Compueto por muchas redes pequeñas unidas entre sí)

Bits --> Datos a nivel físico

Transductor de entrada --> Convierte cualquier fenómeno físico que se quiera transmitir en electricidad.

Guayabo -> Árbol de América, de la familia de las mirtáceas, que crece hasta cinco o seis metros de altura, con tronco torcido y ramoso, hojas elípticas, puntiagudas, ásperas y gruesas, flores blancas, olorosas, axilares, de muchos pétalos redondeados, y cuyo fruto es la guayaba.

Galga -> AWG [Medida de gorsor de los cables]

DND -> Domain Name System

> Cuanto menor es el número, más fino será el cable [Ej: AWG 22 es más delgado que AWG 14]

Transmisor --> Prepara dicha electricidad para que pueda viajar por el cable. **corregir

MTU -> Maxim Transfer Unit
NTP -> Network Type Protocol


