# RSA_Mã Hoá
## Nguyên lý chung RSA
Thuật toán RSA đơn giản thực hiện việc mã hóa và giải mã tin nhắn bằng với các bước cơ bản
- Mã hoá bảng chữ cái
  + Khi một ký tự được mã hóa, trước hết nó sẽ được chuyển thành chuỗi số (theo bảng alphabet_e), và sau đó sẽ áp dụng thuật toán RSA lên chuỗi số này.
- Thuật toán Euclid: Tìm ƯCLN
  + Việc tính ƯCLN đảm bảo rằng số e (số mũ trong khóa công khai) và φ(n) không có ước chung nào lớn hơn 1, đảm bảo tính bảo mật của thuật toán RSA.
- Tạo khóa mã hóa và giải mã
  + RSA hoạt động dựa trên việc tính toán từ hai số nguyên tố lớn để tạo ra khóa mã hóa (công khai) và khóa giải mã (bí mật).
## Giao diện trong Terminal
- Tạo cặp khóa RSA
- Mã hóa tin nhắn trong terminal
- Giải mã tin nhắn trong terminal
## Giao diện GUI
![image](https://github.com/user-attachments/assets/1e50fe3e-7a96-4f8f-99fe-761e641d509b)
