import hashlib
import time

class Transaction:
    def __init__(self, sender, recipient, amount, required_signatures):
        self.sender = sender                 # Địa chỉ người gửi
        self.recipient = recipient           # Địa chỉ người nhận
        self.amount = amount                 # Số lượng coin được chuyển
        self.timestamp = time.time()         # Thời gian tạo giao dịch
        self.transaction_id = self.calculate_hash()   # ID của giao dịch
        self.required_signatures = required_signatures   # Số lượng chữ ký yêu cầu
        self.signatures = []                 # Danh sách các chữ ký số từ các bên tham gia

    def calculate_hash(self):
        # Tạo chuỗi dữ liệu của giao dịch bằng cách kết hợp các thuộc tính của giao dịch thành một chuỗi duy nhất
        data_str = str(self.sender) + str(self.recipient) + str(self.amount) + str(self.timestamp)
        # Sử dụng hàm hash SHA-256 để tạo hash của chuỗi dữ liệu
        return hashlib.sha256(data_str.encode()).hexdigest()

    def sign_transaction(self, private_key):
        # Tạo chữ ký số cho giao dịch bằng cách sử dụng private key của người gửi
        signature = private_key.sign(self.calculate_hash())
        self.signatures.append(signature)

    def verify_transaction(self, public_key):
        # Kiểm tra tính hợp lệ của số lượng chữ ký yêu cầu
        if len(self.signatures) < self.required_signatures:
            return False
        # Kiểm tra tính hợp lệ của tất cả các chữ ký số
        for signature in self.signatures:
            if self.sender != public_key.verify(signature):
                return False
        return True

    @staticmethod
    def check_balance(address, blockchain):
        # Kiểm tra số dư của một địa chỉ trong blockchain
        balance = 0
        for block in blockchain.chain:
            for transaction in block.transactions:
                if transaction.sender == address:
                    balance -= transaction.amount
                elif transaction.recipient == address:
                    balance += transaction.amount
        return balance

# Test code
if __name__ == "__main__":
    # Tạo một giao dịch mới yêu cầu từ 5 đến 20 chữ ký
    transaction = Transaction("sender_address", "recipient_address", 10, 5)
    # In ra ID của giao dịch
    print("Transaction ID:", transaction.transaction_id)
