import time
from .block import Block

# Tạo một khối mới
block = Block(0, "0", time.time(), "đây là khởi nguồn của kết thúc, chúc bạn may mắn lần sau")
timestamp_before = block.timestamp


# In ra hash của khối trước khi đào
print("Hash before mining:", block.hash)

# Thử đào khối với độ khó là 2
block.mine_block(2)

# In ra hash của khối sau khi đào
print("Hash after mining:", block.hash)
print("nonce:", block.nonce)
print("timestamp", block.timestamp - timestamp_before) 