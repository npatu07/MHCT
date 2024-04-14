class SmartContract:
    def __init__(self):
        self.contract_state = {}  # Lưu trữ trạng thái của smart contract

    def execute_transaction(self, sender, recipient, amount):
        """
        Thực hiện giao dịch và cập nhật trạng thái của smart contract
        :param sender: <str> Địa chỉ người gửi
        :param recipient: <str> Địa chỉ người nhận
        :param amount: <int> Số lượng coin được chuyển
        :return: <bool> True nếu giao dịch thành công, False nếu giao dịch không thành công
        """
        # Kiểm tra xem người gửi có đủ số dư để thực hiện giao dịch không
        if self.check_balance(sender, amount):
            # Thực hiện chuyển coin từ người gửi đến người nhận
            self.update_balance(sender, -amount)
            self.update_balance(recipient, amount)
            return True
        else:
            return False

    def check_balance(self, address, amount):
        """
        Kiểm tra xem người dùng có đủ số dư để thực hiện giao dịch không
        :param address: <str> Địa chỉ người dùng
        :param amount: <int> Số lượng coin cần chuyển
        :return: <bool> True nếu có đủ số dư, False nếu không đủ số dư
        """
        if address in self.contract_state:
            return self.contract_state[address] >= amount
        else:
            # Trả về False nếu địa chỉ không tồn tại trong smart contract
            return False

    def update_balance(self, address, amount):
        """
        Cập nhật số dư của một địa chỉ trong smart contract
        :param address: <str> Địa chỉ người dùng
        :param amount: <int> Số lượng coin cần cập nhật
        :return: None
        """
        if address in self.contract_state:
            self.contract_state[address] += amount
        else:
            # Tạo một số dư mới nếu địa chỉ không tồn tại trong smart contract
            self.contract_state[address] = amount
