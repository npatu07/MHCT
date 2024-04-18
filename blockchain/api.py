from flask import Flask, request
from .blockchain import Blockchain
from .smart_contract import SmartContract

class BlockchainAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.blockchain = Blockchain()
        self.smart_contract = SmartContract()
        self.app.add_url_rule('/new_transaction', 'new_transaction', self.new_transaction, methods=['POST'])
        self.app.add_url_rule('/chain', 'full_chain', self.full_chain, methods=['GET'])

    def new_transaction(self):
        values = request.get_json()

        # Kiểm tra xem các trường cần thiết có trong dữ liệu POST không
        required = ['sender', 'recipient', 'amount']
        if not all(k in values for k in required):
            return 'Missing values', 400

        # Tạo một giao dịch mới
        index = self.blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

        response = {'message': f'Transaction will be added to Block {index}'}
        return response, 201

    def full_chain(self):
        response = {
            'chain': self.blockchain.chain,
            'length': len(self.blockchain.chain),
        }
        return response, 200

    def run(self):
        self.app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    api = BlockchainAPI()
    api.run()