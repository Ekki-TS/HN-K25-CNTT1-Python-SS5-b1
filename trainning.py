"""
        1. Các câu lệnh điều khiển vòng lặp
        + break
        + continue
        2. Vòng lặp lồng nhau (nested loop)
        3. Dùng code để vẽ hình

"""


"""
    1. break dung de thoat vong lặp.
    2. viet code sau break không có ý nghĩa.
    3. ví dụ
        Muốn tạo một game đoán số 
        Tạo mặc định 1 số 1-10 
        Sau đó cho người dùng nhập 1 số bất kì 
            + Nếu số người dùng nhập trùng với số ban đầu thì in ra bạn đã chiến thắng 
            + Nếu sai cho người dùng nhập

"""

"""
secret = 5
while True:
    number = int(input("Mời bạn nhập số: "))
    if number == secret:
        print("Bạn đã chọn đúng!")
        break
    print("Đoán sai r!")

"""

"""
Vòng lặp lồng nhau:
Bên trong vòng lặp lại có vòng lặp
ứng dụng:
+ xử ly các bai toán về thuật toán
+ duyệt các phần tử nhiều cấp
+ vẽ hình
Note:
các viết vòng lặp lồng nhau
luồng thực thi
"""
"""
    
"""

for i in range (5):
    for j in range (i + 1):
        print("*", end="")
    print()