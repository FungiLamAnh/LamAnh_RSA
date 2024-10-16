import tkinter as tk
from tkinter import messagebox

# Mã Hoá Bảng Chữ Cái
alphabet_e = {
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
    '0': '093', '1': '094', '2': '095', '3': '096', '4': '097',
    '5': '098', '6': '099', '7': '100', '8': '101', '9': '102',
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
    n = p * q
    N0 = (p - 1) * (q - 1)
    for i in range(2, N0):
        if gcd(i, N0) == 1:
            e = i
            break
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
    plaintext = msg.lower().split()
    encrypted = []
    for word in plaintext:
        chars = split(word)
        encrypted_chars = [encrypt(alphabet_e[char], N, e) for char in chars]
        encrypted_word = " ".join(encrypted_chars)
        encrypted.append(encrypted_word)
    encrypted = f" {encrypt(alphabet_e[' '], N, e)} ".join(encrypted)
    return encrypted

# Giải mã tin nhắn
def decrypt_message(msg, N, d):
    encrypted = msg.split()
    decrypted = []
    plaintext = []
    for char in encrypted:
        decrypted.append(decrypt(char, N, d))
    for char in decrypted:
        plaintext.append(alphabet_d[char])
    return "".join(plaintext)

# Hàm xử lý mã hóa
def handle_encrypt():
    try:
        N = int(entry_n_encrypt.get())
        e = int(entry_e_encrypt.get())
        message = entry_message_encrypt.get()
        encrypted_msg = encrypt_message(message, N, e)
        entry_result_encrypt.delete(0, tk.END)
        entry_result_encrypt.insert(0, encrypted_msg)
    except Exception as ex:
        messagebox.showerror("Error", "Đã có lỗi xảy ra! Vui lòng kiểm tra lại dữ liệu nhập.")
        print(ex)

# Hàm xử lý giải mã
def handle_decrypt():
    try:
        N = int(entry_n_decrypt.get())
        d = int(entry_d_decrypt.get())
        message = entry_message_decrypt.get()
        decrypted_msg = decrypt_message(message, N, d)
        entry_result_decrypt.delete(0, tk.END)
        entry_result_decrypt.insert(0, decrypted_msg)
    except Exception as ex:
        messagebox.showerror("Error", "Đã có lỗi xảy ra! Vui lòng kiểm tra lại dữ liệu nhập.")
        print(ex)

# Hàm tạo khóa mã hóa và giải mã
def handle_generate_keys():
    try:
        p = int(entry_p.get())
        q = int(entry_q.get())
        N, e, d = generate_keys(p, q)
        entry_n_key.delete(0, tk.END)
        entry_e_key.delete(0, tk.END)
        entry_d_key.delete(0, tk.END)
        entry_n_key.insert(0, str(N))
        entry_e_key.insert(0, str(e))
        entry_d_key.insert(0, str(d))
    except Exception as ex:
        messagebox.showerror("Error", "Đã có lỗi xảy ra! Vui lòng kiểm tra lại các số nguyên tố.")
        print(ex)

# Tạo giao diện UI
root = tk.Tk()
root.title("Mã hóa/Giải mã RSA")

# Frame Tạo khóa
frame_key = tk.LabelFrame(root, text="Tạo Khóa", padx=20, pady=20)
frame_key.pack(padx=10, pady=10)

tk.Label(frame_key, text="Số nguyên tố p:").grid(row=0, column=0)
entry_p = tk.Entry(frame_key)
entry_p.grid(row=0, column=1)

tk.Label(frame_key, text="Số nguyên tố q:").grid(row=1, column=0)
entry_q = tk.Entry(frame_key)
entry_q.grid(row=1, column=1)

tk.Label(frame_key, text="N:").grid(row=2, column=0)
entry_n_key = tk.Entry(frame_key)
entry_n_key.grid(row=2, column=1)

tk.Label(frame_key, text="e:").grid(row=3, column=0)
entry_e_key = tk.Entry(frame_key)
entry_e_key.grid(row=3, column=1)

tk.Label(frame_key, text="d:").grid(row=4, column=0)
entry_d_key = tk.Entry(frame_key)
entry_d_key.grid(row=4, column=1)

button_generate_keys = tk.Button(frame_key, text="Tạo Khóa", command=handle_generate_keys)
button_generate_keys.grid(row=5, column=0, columnspan=2)

# Frame Mã hóa
frame_encrypt = tk.LabelFrame(root, text="Mã hóa", padx=20, pady=20)
frame_encrypt.pack(padx=10, pady=10)

tk.Label(frame_encrypt, text="N:").grid(row=0, column=0)
entry_n_encrypt = tk.Entry(frame_encrypt)
entry_n_encrypt.grid(row=0, column=1)

tk.Label(frame_encrypt, text="e:").grid(row=1, column=0)
entry_e_encrypt = tk.Entry(frame_encrypt)
entry_e_encrypt.grid(row=1, column=1)

tk.Label(frame_encrypt, text="Tin nhắn:").grid(row=2, column=0)
entry_message_encrypt = tk.Entry(frame_encrypt, width=40)
entry_message_encrypt.grid(row=2, column=1)

tk.Label(frame_encrypt, text="Kết quả mã hóa:").grid(row=3, column=0)
entry_result_encrypt = tk.Entry(frame_encrypt, width=40)
entry_result_encrypt.grid(row=3, column=1)

button_encrypt = tk.Button(frame_encrypt, text="Mã hóa", command=handle_encrypt)
button_encrypt.grid(row=4, column=0, columnspan=2)

# Frame Giải mã
frame_decrypt = tk.LabelFrame(root, text="Giải mã", padx=20, pady=20)
frame_decrypt.pack(padx=10, pady=10)

tk.Label(frame_decrypt, text="N:").grid(row=0, column=0)
entry_n_decrypt = tk.Entry(frame_decrypt)
entry_n_decrypt.grid(row=0, column=1)

tk.Label(frame_decrypt, text="d:").grid(row=1, column=0)
entry_d_decrypt = tk.Entry(frame_decrypt)
entry_d_decrypt.grid(row=1, column=1)

tk.Label(frame_decrypt, text="Tin nhắn đã mã hóa:").grid(row=2, column=0)
entry_message_decrypt = tk.Entry(frame_decrypt, width=40)
entry_message_decrypt.grid(row=2, column=1)

tk.Label(frame_decrypt, text="Kết quả giải mã:").grid(row=3, column=0)
entry_result_decrypt = tk.Entry(frame_decrypt, width=40)
entry_result_decrypt.grid(row=3, column=1)

button_decrypt = tk.Button(frame_decrypt, text="Giải mã", command=handle_decrypt)
button_decrypt.grid(row=4, column=0, columnspan=2)

root.mainloop()
