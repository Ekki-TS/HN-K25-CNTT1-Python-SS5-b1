employee = int(input("Nhập số lượng nhân viên: "))

for i in range(1, employee + 1):
    name = str(input(f"\nNhập tên nhân viên thứ {i}: "))
    work_day = int(input("Nhập số ngày làm: "))

    if work_day < 0 or work_day > 22:
        print("Dữ liệu không hợp lệ")
        continue
    
    elif work_day == 0:
        print(f"Nhân viên {name} nghỉ toàn bộ tháng")
    
    else:
        for i in range(work_day, work_day + 1):
            for j in range(0, 1):
                print(f"{name}: " + "*" * (i))

        if work_day >= 18:
            print("Làm việc chăm chỉ")
        elif work_day < 10:
            print("Làm việc ít")
        else:
            print("Làm việc bình thường")
