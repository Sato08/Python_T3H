# Python_T3H
# BT1:
- Viết code kiểm tra 1 string có phải là palindrome hay ko? (string đối xứng, viết xuôi hay viết ngược đều như nhau, ko kể viết hoa hay viết thường)
# BT2:
- Các biến liệt kê bên dưới nằm trong đoạn từ 1 đến 9, hỏi có bn bộ giá trị thỏa mãn điều kiện sau:
- a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 = 66
- Viết code thực hiện phép toán trên 1 cách nhanh nhất :)
# BT3:
- Nhập 1 số nguyên trong đoạn từ 1 đến 12, thực hiện trả về tuple bao gồm số ngày và tên tiếng anh tương ứng
input: 1
output: (31, "January")
-nếu nhập ngoài khoảng đó thì thông báo nhập lại, đến khi nào đúng thì thôi.
# BT4:
- Cho đoạn bài hát sau
  + Ngư60ời 'theo hư@ơng' hoa 100mây mù [giăng lối]
  + Làn 25 sương khó30i phôi phai 90 đưa bư$ớc ai xa rồi 35
  + 100Đơn c#ôi m99ình ta {vấn vương} hồi ức tro^ng ... men say (chiều mưa) buồ80n 
  + Ng~ăn "giọt lệ" ngừng k2hiến khoé mi sầu bi.1 
- làm rõ lời bài hát bằng cách loại bỏ toàn bộ các số và kí tự puntuation :)
- puntuation là gì?
-  import string
string.puntuation # :)
# BT5:
- Trả về 1 list n tuple được định nghĩa như sau:
  + years = [(1900, "Canh Tí"), ... (2019, "Kỷ Hợi")]
- với năm chạy từ 1900 đến 2019, output yêu cầu trả về đúng như format bên trên, bao gồm năm và can chi tương ứng
- Chú ý viết hoa các chữ cái đầu
# BT6:
- Viết code sinh các số fibonanci dưới 1000, lưu giữ kq vào 1 list.
# BT7:
- Viết code sinh các số nguyên tố dưới 10000, lưu giữ kq vào 1 list.
# BT8:
- Cho 1 list như sau:
  + samples = ["python", None, "cpython", True, 1, 1 + 1j, False, [100, 200, 300], 99.99, (31, "January")]
- Lọc lấy ra các phần từ là số của list samples
# BT9:
- Tạo 1 list chứa 100 phần tử ngẫu nhiên
- Viết code sinh ra 1 list mới chứa bộ n (là 1 tuple) là n phần tử liên tiếp nhau, duyệt lần lượt, các phần tử nào còn thừa ko đủ để tạo bộ n phần tử thì ko add thêm vào list
- Ví dụ:
- numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10....]  # 100 phần tử ngẫu nhiên
- output, với n = 3 là bộ 3 phần tử
- result = [(1, 3, 5), (7, 9, 2), (4, 6, 8), ...]
