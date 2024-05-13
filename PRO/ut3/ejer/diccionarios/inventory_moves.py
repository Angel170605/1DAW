# *************************
# MOVIMIENTOS DE INVENTARIO
# *************************


def run(imoves: str) -> dict:
    inventory = {}
    moves = imoves.split(',')
    for move in moves:
        if move[0] not in inventory.keys():
            inventory[(move[0])] = [int(move[1:])]  
        else:
            move[0] += int(move[1:])

    return inventory


if __name__ == '__main__':
    run('A1,B4,A-2,A7,B1,C4')