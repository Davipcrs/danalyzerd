from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
import binascii


def generate_AESkey(password: str, salt: bytes, key_length: int = 32) -> str:
    """This Function Creates a Key based on the paramenters

        The Return type is the Key on (Str) in Hex Format
    """
    kdf = Scrypt(
        salt=salt,
        length=key_length,
        n=2**14,
        r=8,
        p=5,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    return binascii.hexlify(key).decode()
