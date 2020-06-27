import os


def get_bytes(file: str) -> bytes:
    with open(file, 'rb') as f:
        b = f.read()
    return b


def save_bytes(file: str, b: bytes) -> None:
    with open(f'{os.getcwd()}/cache/{file}', 'wb') as f:
        f.write(b)
