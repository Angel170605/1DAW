player_1 = input('Jugador 1: Elije (piedra/papel/tijeras)')
player_2 = input('Jugador 2:Elije (piedra/papel/tijeras)')

match player_1:
    case 'piedra':
        if player_2 == 'piedra':
            print('Empate')
        if player_2 == 'papel':
            print('Gana Jugador 2')
        if player_2 == 'tijeras':
            print('Gana Jugador 1')
    case 'papel':
        if player_2 == 'piedra':
            print('Gana Jugador 1')
        if player_2 == 'papel':
            print('Empate')
        if player_2 == 'tijeras':
            print('Gana Jugador 2')
    case 'tijeras':
        if player_2 == 'piedra':
            print('Gana Jugador 2')
        if player_2 == 'papel':
            print('Gana Jugador 1')
        if player_2 == 'tijeras':
            print('Empate')
