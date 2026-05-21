while True:

    print("\n===== MENU =====")
    print("1. Nhập dữ liệu và xem báo cáo thống kê")
    print("2. Xem hướng dẫn sử dụng")
    print("3. Thoát chương trình")

    choice = int(input("Nhập lựa chọn: "))

    if choice == 1:

        branch_count = int(input("Nhập số lượng chi nhánh: "))

        max_students = -1
        max_branch = 0
        has_low_class = False

        for i in range(branch_count):
            print(f"\n--- Chi nhánh {i + 1} ---")
            class_count = int(input("Nhập số lớp học: "))
            total_students = 0

            for j in range(class_count):
                while True:
                    students = int(input(f"Nhập số học viên lớp {j + 1}: "))
                    if students < 0:
                        print("Số học viên không hợp lệ. Vui lòng nhập lại.")
                    else:
                        break

                total_students += students

                if students < 10:
                    has_low_class = True
                    print(f"Lớp có sĩ số thấp: "f"Chi nhánh {i + 1} - Lớp {j + 1}")
            print(f"Tổng số học viên chi nhánh {i + 1}: "f"{total_students}")

            if total_students > max_students:
                max_students = total_students
                max_branch = i + 1

        print(f"\nChi nhánh có số học viên cao nhất: "f"Chi nhánh {max_branch} ({max_students} học viên)")

        if has_low_class == False:
            print("Không có lớp nào dưới 10 học viên.")

    elif choice == 2:

        print("HƯỚNG DẪN")
        print("1. Cách nhập dữ liệu")
        print("2. Quy tắc thống kê")
    elif choice == 3:
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")