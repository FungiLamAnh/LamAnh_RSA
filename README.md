# RSA_Mã Hoá
## Nguyên lý chung RSA
Thuật toán RSA đơn giản thực hiện việc mã hóa và giải mã tin nhắn bằng với các bước cơ bản
- Mã hoá bảng chữ cái
  + Khi một ký tự được mã hóa, trước hết nó sẽ được chuyển thành chuỗi số (theo bảng alphabet_e), và sau đó sẽ áp dụng thuật toán RSA lên chuỗi số này.
- Thuật toán Euclid: Tìm ƯCLN
  + Việc tính ƯCLN đảm bảo rằng số e (số mũ trong khóa công khai) và φ(n) không có ước chung nào lớn hơn 1, đảm bảo tính bảo mật của thuật toán RSA.
- Tạo khóa mã hóa và giải mã
  + RSA hoạt động dựa trên việc tính toán từ hai số nguyên tố lớn để tạo ra khóa mã hóa (công khai) và khóa giải mã (bí mật).
- Mã hoá/Giải mã ký tự
  + Mỗi ký tự sẽ được chuyển thành một số nguyên, sau đó áp dụng phép tính RSA (char^e % N) để mã hóa. Từ đó giải mã bằng cách áp dụng phép tính ngược lại với mã hóa (char^d % N), sử dụng khóa bí mật.
- Mã hoá/Giải mã tin nhắn
  + Tin nhắn sẽ được chia nhỏ thành từng ký tự, sau đó mỗi ký tự sẽ được mã hóa và ghép lại thành chuỗi mã hóa. Ngược lại khi giải mã, tin nhắn cũng sẽ được chia nhỏ thành từng phần và giải từng ký tự.
## Hai loại hiển thị
### Giao diện trong Terminal (CLI)
- Tạo cặp khóa RSA
- Mã hóa tin nhắn trong terminal
- Giải mã tin nhắn trong terminal
![image](https://github.com/user-attachments/assets/9ba45f87-62b2-40bb-80ce-d8aa20e3c11c)

### Giao diện GUI
![image](https://github.com/user-attachments/assets/1e50fe3e-7a96-4f8f-99fe-761e641d509b)
