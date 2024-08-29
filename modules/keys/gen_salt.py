from random import SystemRandom


def generate_salt() -> bytes:
    """This function generate a 32 Byte Salt"""
    secure_random = SystemRandom()
    rand_bytes = secure_random.getrandbits(8 * 32)
    rand_bytes = rand_bytes.to_bytes(32, 'big')

    return rand_bytes
