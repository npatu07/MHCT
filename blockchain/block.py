import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index             # Số thứ tự của khối trong chuỗi blockchain
        self.previous_hash = previous_hash   # Hash của khối trước đó
        self.timestamp = timestamp     # Thời gian tạo khối
        self.data = data               # Dữ liệu giao dịch của khối
        self.nonce = nonce             # Số ngẫu nhiên để thực hiện POW
        self.hash = self.calculate_hash()   # Hash của khối hiện tại

    @classmethod
    def calculate_hash(self):
        # Tạo chuỗi dữ liệu của khối bằng cách kết hợp các thuộc tính của khối thành một chuỗi duy nhất
        data_str = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.data) + str(self.nonce)
        # Sử dụng hàm hash SHA-256 để tạo hash của chuỗi dữ liệu
        return hashlib.sha256(data_str.encode()).hexdigest()

    def mine_block(self, difficulty):
        # Tìm nonce sao cho hash của khối có đủ số lượng số 0 đầu tiên
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            print("runing nonce, in mine_block function, file block.py: ",self.nonce) #xem KQ từng step
            self.hash = self.calculate_hash()
            print("caculated hash = ",self.hash) #xem KQ từng step
            time.sleep(0.01) #chậm lại để khỏi lag
        print("Block mined: ", self.hash)

# Test code
if __name__ == "__main__":
    block = Block(0, "0", time.time(), "Genesis Block")
    print("Hash:", block.hash)
    block.mine_block(2)  # Thử đào khối với độ khó là 2
