from .utils import generate_rsa_key_pair, generate_address, sign_message, verify_signature

class Wallet:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.address = None

    def generate_key_pair(self):
        self.private_key, self.public_key = generate_rsa_key_pair()

    def generate_address(self):
        if self.public_key is None:
            raise ValueError("Public key is missing. Generate key pair first.")
        self.address = generate_address(self.public_key)

    def sign_message(self, message):
        if self.private_key is None:
            raise ValueError("Private key is missing. Generate key pair first.")
        return sign_message(self.private_key, message)

    def verify_signature(self, message, signature, public_key):
        return verify_signature(public_key, signature, message)
