import bcrypt

SALTS = bcrypt.gensalt()


def hash_pwd(password: str):
    return bcrypt.hashpw(password.encode(), SALTS).decode()


def check_password(password: str, hash_password: str):
    return bcrypt.checkpw(password.encode(), hash_password.encode())
