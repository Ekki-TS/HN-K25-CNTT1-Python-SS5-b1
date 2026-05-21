branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

for branch in range(1, branch_count + 1):
    print(f"Chi nhánh {branch}")

    for month in range(1, month_count + 1):
        revenue = int(
            input(f"Nhập doanh thu Chi nhánh {branch}, "f"tháng {month}: ")
        )

        print(f"Chi nhánh {branch}, tháng {month}: "f"{revenue} triệu đồng")
