branch = int(input("Nhập số lượng chi nhánh: "))

for i in range(branch):
    print(f"Chi nhánh {i + 1}")

    for j in range(2):

        while True: 
            student = int(input(f"Nhập số học viên đi học của lớp {j + 1}: "))

            if student < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")
            else:
                break

        if student == 0:
            print("Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
        elif student >= 20:
            print(f"Chi nhánh {i + 1} - Lớp {j + 1}: Lớp học ổn định")
        else:
            print(f"Chi nhánh {i + 1} - Lớp {j + 1}: Lớp cần được nhắc nhở theo dõi")