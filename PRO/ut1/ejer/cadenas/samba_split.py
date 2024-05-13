# ***********************
# SEPARANDO RECURSO SAMBA
# ***********************


def run(smb_path: str) -> tuple:
    host = smb_path[:/]
    variable = len(host)
    path = smb_path[variable:]

    return host, path


if __name__ == '__main__':
    run('//1.1.1.1/aprende/python')
