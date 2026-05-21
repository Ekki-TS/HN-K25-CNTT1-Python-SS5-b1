classroom = int(input("Nhập số lượng phòng học cần kiểm tra: "))

if classroom <= 0:
    print("Số lượng phòng không hợp lệ!")

for i in range (1, classroom + 1):
    print(f"Phòng thứ: {i}")
    chair_room = int(input("Nhập số hàng ghế của từng phòng: "))
    chair_row = int(input("Nhập số ghế trên mỗi hàng: "))
    
    if chair_room <= 0 or chair_row <= 0:
        print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
        continue
    elif chair_room > 10 or chair_row > 10:
        print("Phòng quá lớn. Dừng nhập dữ liệu")
        break
    else: 
        for i in range(chair_room):
            for j in range(0, chair_row):
                print("*" , end = "")
            print()
            