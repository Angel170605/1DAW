age = int(input('Introduzca su edad '))
weight = int(input('Intruduzca su peso '))
pulse = int(input('Introduzca su pulso '))
platelet = int(input('Introduzca sus plaquetas '))

if 18 <= age <= 65 and weight > 50 and 50 <= pulse <= 110 and platelet > 150.000:
    print('Apto para donar sangre')
else:
    print('No apto para donar sangre')
