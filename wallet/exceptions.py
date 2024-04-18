#14 exceptions
class WalletError(Exception):
    """Lớp cơ sở cho tất cả các ngoại lệ trong phần Wallet."""

    def __init__(self, message="Lỗi Wallet!"):
        self.message = message
        super().__init__(self.message)

class KeyNotFoundError(WalletError):
    """Ngoại lệ xảy ra khi không tìm thấy khóa công khai hoặc khóa riêng tư liên quan đến một địa chỉ ví cụ thể."""

    def __init__(self, message="Không tìm thấy khóa!"):
        self.message = message
        super().__init__(self.message)

class InvalidSignatureError(WalletError):
    """Ngoại lệ xảy ra khi chữ ký của giao dịch hoặc thông điệp không hợp lệ."""

    def __init__(self, message="Chữ ký không hợp lệ!"):
        self.message = message
        super().__init__(self.message)

class PermissionError(WalletError):
    """Ngoại lệ xảy ra khi người dùng không có quyền truy cập vào một hoặc nhiều chức năng hoặc tài nguyên của ví."""

    def __init__(self, message="Không có quyền truy cập!"):
        self.message = message
        super().__init__(self.message)

class TimeoutError(WalletError):
    """Ngoại lệ xảy ra khi một yêu cầu của người dùng vượt quá thời gian chờ quy định."""

    def __init__(self, message="Yêu cầu vượt quá thời gian chờ!"):
        self.message = message
        super().__init__(self.message)

class DataIntegrityError(WalletError):
    """Ngoại lệ xảy ra khi dữ liệu trong ví bị thay đổi hoặc bị hỏng mà không được mong đợi."""

    def __init__(self, message="Dữ liệu không hợp lệ!"):
        self.message = message
        super().__init__(self.message)

class StorageError(WalletError):
    """Ngoại lệ xảy ra khi có lỗi xảy ra trong quá trình lưu trữ hoặc truy xuất dữ liệu của ví."""

    def __init__(self, message="Lỗi lưu trữ dữ liệu!"):
        self.message = message
        super().__init__(self.message)

class ConfigurationError(WalletError):
    """Ngoại lệ xảy ra khi cấu hình của ví không đúng hoặc không hợp lệ."""

    def __init__(self, message="Cấu hình không hợp lệ!"):
        self.message = message
        super().__init__(self.message)

class InvalidAddressError(WalletError):
    """Ngoại lệ xảy ra khi một địa chỉ ví không hợp lệ được cung cấp."""

    def __init__(self, message="Địa chỉ ví không hợp lệ!"):
        self.message = message
        super().__init__(self.message)

class DuplicateTransactionError(WalletError):
    """Ngoại lệ xảy ra khi một giao dịch đã tồn tại trong ví và cố gắng thêm một lần nữa."""

    def __init__(self, message="Giao dịch đã tồn tại trong ví!"):
        self.message = message
        super().__init__(self.message)

class EncryptionError(WalletError):
    """Ngoại lệ xảy ra khi có lỗi trong quá trình mã hóa hoặc giải mã dữ liệu trong ví."""

    def __init__(self, message="Lỗi mã hóa/giải mã dữ liệu trong ví!"):
        self.message = message
        super().__init__(self.message)

class NetworkError(WalletError):
    """Ngoại lệ xảy ra khi có lỗi liên quan đến kết nối mạng."""

    def __init__(self, message="Lỗi kết nối mạng!"):
        self.message = message
        super().__init__(self.message)

class InsufficientFundsError(WalletError):
    """Ngoại lệ xảy ra khi người dùng không đủ tiền trong tài khoản để thực hiện giao dịch."""

    def __init__(self, message="Số dư không đủ để thực hiện giao dịch!"):
        self.message = message
        super().__init__(self.message)

class WalletNotFoundError(WalletError):
    """Ngoại lệ xảy ra khi không tìm thấy ví trong cơ sở dữ liệu hoặc truy vấn không thành công."""

    def __init__(self, message="Không tìm thấy ví!"):
        self.message = message
        super().__init__(self.message)
