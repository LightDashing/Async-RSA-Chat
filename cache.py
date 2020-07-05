import os
import webbrowser as wb


def get_bytes(file: str) -> bytes:
    with open(file, 'rb') as f:
        b = f.read()
    return b


def save_bytes(file: str, b: bytes) -> None:
    with open(f'{os.getcwd()}/cache/{file}', 'wb') as f:
        f.write(b)


def clear_cache() -> None:
    fullpath = f'{os.getcwd()}/cache/'
    for file in os.listdir(fullpath):
        os.remove(f'{fullpath}/{file}')
