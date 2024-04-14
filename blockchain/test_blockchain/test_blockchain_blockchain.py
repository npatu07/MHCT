from blockchain.blockchain import Blockchain

# Tạo một blockchain mới
blockchain = Blockchain()

# Tạo một giao dịch mới
blockchain.new_transaction("sender1", "recipient1", 10)

# Tìm proof of work mới
last_block = blockchain.last_block
last_proof = last_block['proof']
proof = blockchain.proof_of_work(last_proof)

# Thêm block mới vào blockchain
previous_hash = blockchain.hash(last_block)
block = blockchain.new_block(proof, previous_hash)

# In ra blockchain sau khi thêm block mới
print("Updated Blockchain:")
print(blockchain.chain)
