import hashlib
import uuid

class Address:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.address = None

    def generate_address(self):
        """Tạo một địa chỉ ví mới bằng cách tạo cặp khóa công khai và khóa riêng tư."""
        self.private_key = self.generate_private_key()
        self.public_key = self.generate_public_key()
        self.address = self.generate_address_from_public_key()

    def generate_private_key(self):
        """Tạo một khóa riêng tư ngẫu nhiên."""
        return str(uuid.uuid4())

    def generate_public_key(self):
        """Tạo một khóa công khai từ khóa riêng tư."""
        return hashlib.sha256(self.private_key.encode()).hexdigest()

    def generate_address_from_public_key(self):
        """Tạo địa chỉ ví từ khóa công khai."""
        return hashlib.sha256(self.public_key.encode()).hexdigest()

    def get_address(self):
        """Trả về địa chỉ ví."""
        return self.address

    def get_private_key(self):
        """Trả về khóa riêng tư."""
        return self.private_key

    def get_public_key(self):
        """Trả về khóa công khai."""
        return self.public_key
