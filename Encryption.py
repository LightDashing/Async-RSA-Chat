from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes


def encrypt(public_key, message: str) -> list:
    session_key = get_random_bytes(16)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    enc_session_key = cipher_rsa.encrypt(session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    cipher_text, tag = cipher_aes.encrypt_and_digest(message.encode("utf-8"))
    message = []
    [message.append(x) for x in (enc_session_key, cipher_aes.nonce, tag, cipher_text)]
    return message


def encrypt_bytes(public_key, message: bytes) -> list:
    session_key = get_random_bytes(16)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    enc_session_key = cipher_rsa.encrypt(session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    cipher_text, tag = cipher_aes.encrypt_and_digest(message)
    message = []
    [message.append(x) for x in (enc_session_key, cipher_aes.nonce, tag, cipher_text)]
    return message


def decrypt(private_key, message: bytes) -> str:
    enc_session_key, nonce, tag, cipher_text = \
        [message[x] for x in range(4)]
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    message = cipher_aes.decrypt_and_verify(cipher_text, tag)
    message = str(message.decode('utf-8'))
    return message


def decrypt_bytes(private_key, message: bytes) -> bytes:
    enc_session_key, nonce, tag, cipher_text = \
        [message[x] for x in range(4)]
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    message = cipher_aes.decrypt_and_verify(cipher_text, tag)
    return message
