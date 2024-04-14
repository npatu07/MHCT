# Import SmartContract class từ file smart_contract.py
from blockchain.smart_contract import SmartContract

# Tạo một smart contract mới
smart_contract = SmartContract()

# Thực hiện giao dịch từ sender đến recipient
sender = "sender_address"
recipient = "recipient_address"
amount = 10
success = smart_contract.execute_transaction(sender, recipient, amount)

if success:
    print("Transaction successful!")
else:
    print("Transaction failed!")
