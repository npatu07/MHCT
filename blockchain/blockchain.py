import hashlib
import json
from time import time
from urllib.parse import urlparse
import requests


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()

        # Tạo block genesis
        self.new_block(previous_hash="1", proof=100)

    def register_node(self, address):
        """
        Thêm một node mới vào danh sách node
        :param address: <str> Địa chỉ của node. VD: 'http://192.168.0.5:5000'
        :return: None
        """
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def valid_chain(self, chain):
        """
        Kiểm tra tính hợp lệ của blockchain
        :param chain: <list> Blockchain
        :return: <bool> True nếu hợp lệ, False nếu không
        """
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f"{last_block}")
            print(f"{block}")
            print("\n-----------\n")
            # Kiểm tra hash của block là đúng
            if block['previous_hash'] != self.hash(last_block):
                return False

            # Kiểm tra proof of work
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self):
        """
        Thuật toán dễ nhất là chấp nhận mạng có chuỗi dài nhất.
        :return: <bool> True nếu chuỗi của chúng ta đã được thay thế, False nếu không
        """

        neighbours = self.nodes
        new_chain = None

        # Chỉ tìm chuỗi dài hơn của chúng ta
        max_length = len(self.chain)

        # Kiểm tra tất cả chuỗi từ tất cả các node trong mạng
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Kiểm tra xem chuỗi có dài hơn và có hợp lệ không
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        # Nếu chúng ta tìm thấy chuỗi mới dài hơn và hợp lệ, thì thay thế chuỗi của chúng ta
        if new_chain:
            self.chain = new_chain
            return True

        return False

    def new_block(self, proof, previous_hash):
        """
        Tạo một block mới trong blockchain
        :param proof: <int> Proof of work của block mới
        :param previous_hash: (Optional) <str> Hash của block trước đó
        :return: <dict> Block mới
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset danh sách giao dịch hiện tại
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Tạo một giao dịch mới để vào block tiếp theo
        :param sender: <str> Địa chỉ người gửi
        :param recipient: <str> Địa chỉ người nhận
        :param amount: <int> Số lượng coin được chuyển
        :return: <int> Index của block chứa giao dịch
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Tạo một SHA-256 hash của một block
        :param block: <dict> Block
        :return: <str>
        """

        # Đảm bảo từ điển của block được sắp xếp, để tránh sự không nhất quán của hash
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        Tìm một số P' mà hash của (PP') chứa 4 số 0 ở đầu
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Kiểm tra xem hash(last_proof, proof) có chứa 4 số 0 ở đầu không
        :param last_proof: <int> Proof cũ
        :param proof: <int> Proof mới
        :return: <bool> True nếu đúng, False nếu sai
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"


# Test code
if __name__ == "__main__":
    blockchain = Blockchain()
    print("Initial Blockchain:")
    print(blockchain.chain)
    print("\n")

    # Tạo một giao dịch mới
    blockchain.new_transaction("sender1", "recipient1", 10)

    # Tìm proof of work mới
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # Thêm block mới vào blockchain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    print("Updated Blockchain:")
    print(blockchain.chain)
