from blockchain.blockchain import Blockchain
from wallet.wallet import Wallet
from wallet.address import Address

class FullNode:
    def __init__(self):
        self.blockchain = Blockchain()
        self.wallet = Wallet()
        self.address = Address()
        self.address.generate_address()

    def register_with_blockchain(self):
        self.blockchain.register_node(self.address.get_address())

    def receive_transaction(self, transaction):
        # Validate the transaction
        if self.blockchain.validate_transaction(transaction):
            # If valid, add to the pool of unconfirmed transactions
            self.blockchain.add_transaction(transaction)
            return True
        return False

    def mine_block(self):
        # Mine a new block from the pool of unconfirmed transactions
        new_block = self.blockchain.mine()
        if new_block:
            return True
        return False

    def receive_new_block(self, block):
        # Validate the received block
        if self.blockchain.validate_block(block):
            # If valid, add to the blockchain
            self.blockchain.add_block(block)
            return True
        return False

    def resolve_conflicts(self, chains):
        # Resolve any conflicts between the current blockchain and other chains
        self.blockchain.resolve_conflicts(chains)