# Mã Hoá Bảng Chữ Cái
alphabet_e = {
    # Ký tự chữ
    'a': '001', 'ă': '002', 'â': '003', 'b': '004', 'c': '005',
    'd': '006', 'đ': '007', 'e': '008', 'ê': '009', 'f': '010',
    'g': '011', 'h': '012', 'i': '013', 'k': '014', 'l': '015',
    'm': '016', 'n': '017', 'o': '018', 'ô': '019', 'ơ': '020',
    'p': '021', 'q': '022', 'r': '023', 's': '024', 't': '025',
    'u': '026', 'ư': '027', 'v': '028', 'w': '029', 'x': '030',
    'y': '031', 'á': '032', 'à': '033', 'ả': '034', 'ã': '035',
    'ạ': '036', 'ấ': '037', 'ầ': '038', 'ẩ': '039', 'ẫ': '040',
    'ậ': '041', 'ắ': '042', 'ằ': '043', 'ẳ': '044', 'ẵ': '045',
    'ặ': '046', 'é': '047', 'è': '048', 'ẻ': '049', 'ẽ': '050',
    'ẹ': '051', 'ế': '052', 'ề': '053', 'ể': '054', 'ễ': '055',
    'ệ': '056', 'í': '057', 'ì': '058', 'ỉ': '059', 'ĩ': '060',
    'ị': '061', 'ó': '062', 'ò': '063', 'ỏ': '064', 'õ': '065',
    'ọ': '066', 'ố': '067', 'ồ': '068', 'ổ': '069', 'ỗ': '070',
    'ộ': '071', 'ớ': '072', 'ờ': '073', 'ở': '074', 'ỡ': '075',
    'ợ': '076', 'ú': '077', 'ù': '078', 'ủ': '079', 'ũ': '080',
    'ụ': '081', 'ứ': '082', 'ừ': '083', 'ử': '084', 'ữ': '085',
    'ự': '086', 'ý': '087', 'ỳ': '088', 'ỷ': '089', 'ỹ': '090',
    'ỵ': '091', ' ': '092',
    # Ký tự số
    '0': '093', '1': '094', '2': '095', '3': '096', '4': '097',
    '5': '098', '6': '099', '7': '100', '8': '101', '9': '102',
    # Ký tự đặc biệt
    ',': '103', '.': '104', '!': '105', '?': '106', ':': '107',
    ';': '108', '-': '109', '_': '110', '(': '111', ')': '112',
    '"': '113', "'": '114', '@': '115', '#': '116', '$': '117',
    '%': '118', '^': '119', '&': '120', '*': '121', '+': '122',
    '=': '123', '/': '124', '\\': '125', '|': '126', '{': '127',
    '}': '128', '[': '129', ']': '130', '<': '131', '>': '132'
}

# Giải Mã Bảng Chữ Cái
alphabet_d = {v: k for k, v in alphabet_e.items()}

# Thuật toán Euclid: Tìm ƯCLN của 2 số
def gcd(a, b):
    if (b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)

# Tạo khóa mã hóa, bao gồm e và d
def generate_keys(p, q):
    # Phần khóa công khai
    n = p * q

    # Phần khóa bí mật
    N0 = (p - 1) * (q - 1)

    # Tìm e: số nguyên đầu tiên nguyên tố cùng nhau với N0
    for i in range(2, N0):
        if gcd(i, N0) == 1:
            e = i
            break

    # Tìm d: nghịch đảo của e theo modulo N0
    for i in range(0, N0):
        if ((e * i) % N0) == 1:
            d = i
            break

    return n, e, d

# Mã hóa ký tự
def encrypt(char, N, e):
    return str((int(char) ** e) % N).zfill(3)

# Giải mã ký tự
def decrypt(char, N, d):
    return str((int(char) ** d) % N).zfill(3)

# Tách từ thành các ký tự
def split(word):
    return [char for char in word]

# Mã hóa tin nhắn
def encrypt_message(msg, N, e):
    # Tin nhắn
    plaintext = msg.lower().split()
    encrypted = []

    # Mã hóa tin nhắn
    for word in plaintext:
        # Tách từ thành ký tự
        chars = split(word)

        # Tạo danh sách các ký tự đã mã hóa
        encrypted_chars = [encrypt(alphabet_e[char], N, e) for char in chars]

        # Thêm từ đã mã hóa vào danh sách
        encrypted_word = " ".join(encrypted_chars)
        encrypted.append(encrypted_word)

    # Nối các từ đã mã hóa với dấu cách
    encrypted = f" {encrypt(alphabet_e[' '], N, e)} ".join(encrypted)

    return encrypted

# Giải mã tin nhắn
def decrypt_message(msg, N, d):
    # Tin nhắn mã hóa
    encrypted = msg.split()
    decrypted = []
    plaintext = []

    # Giải mã
    for char in encrypted:
        decrypted.append(decrypt(char, N, d))

    # Giải mã tin nhắn
    for char in decrypted:
        plaintext.append(alphabet_d[char])

    plaintext = "".join(plaintext)

    return plaintext

# Menu tùy chọn
def options():
    print("Tùy chọn:\n\
        0 - Tạo cặp khóa\n\
        1 - Mã hóa tin nhắn trong terminal\n\
        2 - Giải mã tin nhắn trong terminal\n")

# Giao diện người dùng
while True:

    # Hiển thị tùy chọn
    options()

    # Lấy tùy chọn từ người dùng
    selection = input()

    # Tạo cặp khóa
    if selection == "0":

        # Nhập hai số nguyên tố
        p = int(input("Nhập số nguyên tố thứ nhất: "))
        q = int(input("Nhập số nguyên tố thứ hai: "))
        print()

        try:
            # Tạo khóa công khai và bí mật
            N, e, d = generate_keys(p, q)

            # Hiển thị khóa
            print(f"Khóa công khai:\nN: {N}\ne: {e}\n")
            print(f"Khóa bí mật:\nN: {N}\nd: {d}\n")

        except:
            print("Lỗi: Số nguyên tố không hợp lệ\n")

    # Mã hóa tin nhắn trong terminal
    elif selection == "1":

        # Nhập khóa công khai
        N = int(input("Nhập khóa công khai N: "))
        e = int(input("Nhập khóa công khai e: "))
        print()

        # Nhập tin nhắn
        message = input("Nhập tin nhắn để mã hóa:\n")

        # Hiển thị tin nhắn đã mã hóa
        print(f"\nTin nhắn đã mã hóa:\n{encrypt_message(message, N, e)}\n")

    # Giải mã tin nhắn trong terminal
    elif selection == "2":

        # Nhập khóa bí mật
        N = int(input("Nhập khóa bí mật N: "))
        d = int(input("Nhập khóa bí mật d: "))
        print()

        # Nhập tin nhắn đã mã hóa
        message = input("Nhập tin nhắn để giải mã:\n")

        # Hiển thị tin nhắn đã giải mã
        try:
            print(f"\nTin nhắn đã giải mã:\n{decrypt_message(message, N, d)}\n")
        except:
            print("Lỗi: Khóa bí mật không hợp lệ\n")

    # Kiểm tra đầu vào hợp lệ
    else:
        print("Lựa chọn không hợp lệ\n")

    # Tùy chọn thoát
    exit = input("Bạn có muốn tiếp tục?\n\
        Nhấn 'Y' để tiếp tục\n\
        Nhấn phím bất kỳ để thoát\n").upper()

    print()

    # Tiếp tục nếu người dùng chọn 'Y'
    if exit == "Y":
        continue

    # Thoát chương trình
    else:
        break

