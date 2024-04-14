from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from blockchain.transaction import Transaction
from blockchain.blockchain import Blockchain

# Tạo một cặp khóa RSA mới
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Lưu chuỗi khóa riêng tư và công khai
private_key_str = private_key.decode('utf-8')
public_key_str = public_key.decode('utf-8')

def test_transaction():
    # Tạo một blockchain mới
    blockchain = Blockchain()

    # Tạo đối tượng khóa riêng tư và công khai từ chuỗi
    private_key_obj = RSA.import_key(private_key_str)
    public_key_obj = RSA.import_key(public_key_str)

    # Tạo một giao dịch mới
    transaction = Transaction("sender_address", "recipient_address", 10, 1)

    # Ký giao dịch bằng khóa riêng tư
    hash_obj = SHA256.new(transaction.calculate_hash().encode())
    signer = PKCS1_v1_5.new(private_key_obj)
    signature = signer.sign(hash_obj)
    transaction.signatures.append(signature)

    # Xác minh giao dịch bằng khóa công khai
    hash_obj = SHA256.new(transaction.calculate_hash().encode())
    verifier = PKCS1_v1_5.new(public_key_obj)
    is_valid = verifier.verify(hash_obj, signature)
    assert is_valid == True, "Giao dịch không hợp lệ."

    # Kiểm tra số dư của một địa chỉ trong blockchain
    address_to_check = "address_to_check"
    balance = blockchain.check_balance(address_to_check)
    assert balance == expected_balance, "Số dư không đúng."


if __name__ == "__main__":
    test_transaction()
    print("All tests passed successfully!")