country = (input('Introduzca el nombre de un país')).lower

match country:
    case 'españa':
        print('🇪🇸')
    case 'francia':
        print('🇫🇷')
    case 'portugal':
        print('🇵🇹')
    case 'italia':
        print('🇮🇹')
    case 'estados unidos':
        print('🇺🇸')
    case 'brasil':
        print('🇧🇷')
    case 'argentina':
        print('🇦🇷')
    case 'inglaterra':
        print('🏴󠁧󠁢󠁥󠁮󠁧󠁿')
    case 'alemania':
        print('🇩🇪')
    case _:
        print('Por favor, pruebe con otro país')
