import unittest
import sys

sys.path.append('C:/Users/Admin/OneDrive/Máy tính/MHCT')  # Giữ nguyên đường dẫn

from wallet.utils import generate_rsa_key_pair, generate_address, sign_message, verify_signature
from cryptography.hazmat.primitives.asymmetric import rsa

class TestUtils(unittest.TestCase):
    def test_generate_rsa_key_pair(self):
        private_key, public_key = generate_rsa_key_pair()
        self.assertIsInstance(private_key, rsa.RSAPrivateKey)
        self.assertIsInstance(public_key, rsa.RSAPublicKey)

    def test_generate_address(self):
        private_key, public_key = generate_rsa_key_pair()
        address = generate_address(public_key)
        self.assertEqual(len(address), 64)

    def test_sign_and_verify_message(self):
        private_key, public_key = generate_rsa_key_pair()
        message = b"Test message"
        signature = sign_message(private_key, message)
        self.assertTrue(verify_signature(public_key, signature, message))

        invalid_signature = signature[:-1] + b"X"
        self.assertFalse(verify_signature(public_key, invalid_signature, message))

        modified_message = b"Test message modified"
        self.assertFalse(verify_signature(public_key, signature, modified_message))

if __name__ == '__main__':
    unittest.main()
