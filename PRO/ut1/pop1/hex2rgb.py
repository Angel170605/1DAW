# ***************
# COLORES EN HEXA
# ***************


def run(hex_color: str) -> str:
    hex_red = int(hex_color[:2], 16)
    hex_green = int(hex_color[2:4], 16)
    hex_blue = int(hex_color[4:], 16)

    rgb_color = f'({hex_red},{hex_green},{hex_blue})'

    return rgb_color


if __name__ == '__main__':
    run('A131F7')
