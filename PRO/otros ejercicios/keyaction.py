key_1 = (input('Introduza el nombre de una tecla ')).lower
key_2 = (input('Introduzca el nombre de otra tecla ')).lower
key_3 = (input('Introduzca el nombre de la tercera tecla ')).lower

if key_1 == 'f5' and key_2 == '' and key_3 == '':
    print('Refrescar página')
if key_1 == 'ctrl':
    if key_2 == 'c' and key_3 == '':
        exit = 'Copiar'
    if key_2 == 'x' and key_3 == '':
        exit = 'Cortar'
    if key_2 == 'p' and key_3 == '':
        exit = 'Pegar'
    if key_2 == 'z' and key_3 == '':
        exit = 'Deshacer'
    if key_2 == 'y' and key_3 == '':
        exit = 'Rehacer'
    if key_2 == 'a' and key_3 == '':
        exit = 'Seleccionar todo'
    if key_2 == 's' and key_3 == '':
        exit = 'Guardar'
    if key_2 == 'f' and key_3 == '':
        exit = 'Buscar'
    if key_2 == 'alt' and key_3 == 'supr':
        exit = 'Reiniciar'
    if key_2 == 'n' and key_3 == '':
        exit = 'Abrir nueva ventana en el navegador'
    if key_2 == 'shift' and key_3 == 'n':
        exit = 'Abrir nueva ventana de incógnito en Chrome'
    if key_2 == 'shift' and key_3 == 'p':
        exit = 'Abrir nueva ventana InPrivate en Firefox'
    if key_2 == 't' and key_3 == '':
        exit = 'Abrir nueva pestaña en el navegador'
    if key_2 == 'w' and key_3 == '':
        exit = 'Cerrar pestaña en el navegador'
    if key_2 == 'shift' and key_3 == 't':
        exit = 'Recuperar pestaña cerrada en el navegador'
if key_1 == 'alt':
    if key_2 == 'f4' and key_3 == '':
        exit = 'Cerrar/Apagar equipo'
else:
    exit = 'error, prueba de nuevo'
