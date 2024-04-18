from hashlib import sha256
import time

class Transaction:
    def __init__(self, sender_address, recipient_address, amount, fee, timestamp=None, signature=None):
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.amount = amount
        self.fee = fee
        self.timestamp = timestamp if timestamp else time.time()
        self.signature = signature

    def calculate_hash(self):
        return sha256((str(self.sender_address) + str(self.recipient_address) + str(self.amount) + str(self.fee) + str(self.timestamp)).encode()).hexdigest()

    def sign_transaction(self, private_key):
        message = self.calculate_hash()
        self.signature = private_key.sign(message)

    def verify_transaction(self, public_key):
        message = self.calculate_hash()
        return public_key.verify(message, self.signature)

    def to_dict(self):
        return {
            "sender_address": self.sender_address,
            "recipient_address": self.recipient_address,
            "amount": self.amount,
            "fee": self.fee,
            "timestamp": self.timestamp,
            "signature": self.signature
        }
