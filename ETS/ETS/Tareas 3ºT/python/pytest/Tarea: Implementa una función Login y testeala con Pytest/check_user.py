def check_user_info(user, check_user, password, check_password):
    if user != check_user:
        return f'Error. Los nombres de usuario no coinciden.'
    if password != check_password:
        return f'Error. Las contraseñas no coinciden.'
    return f'Información verificada.'