# 1. Lỗi IndexError tại SofM:
# -> Levi có 3 phần tử, truy cập p[2] (chỉ số 2) lấy được điểm MMR bình thường.
# -> SofM chỉ có 2 phần tử (chỉ số 0 và 1). Truy cập p[2] vượt quá giới hạn mảng gây sập.

# 2. Lỗi tiềm ẩn tại Optimus (ValueError):
# -> Sẽ sập tại dòng: b = (m * 10) + (int(r) * 0.5) do ép kiểu int("N/A").
# -> Tên ngoại lệ xuất hiện trên Console: ValueError.

# 3. Kỹ năng Debug bằng lệnh print():
# -> Giúp biết chính xác chương trình đang chạy đến tuyển thủ nào ngay trước khi sập.
# -> Khoanh vùng được bản ghi dữ liệu lỗi (SofM) để xử lý mà không cần đoán mò.

# 4. Đổi tên biến chuẩn Clean Code:
# -> ds -> player_records | p -> record | t -> name
# -> m  -> matches        | r -> mmr    | b -> bonus_rp


player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]

def calculate_bonus(matches, mmr):
    """Hàm độc lập tính toán điểm thưởng RP theo nguyên tắc mô-đun"""
    return (matches * 10) + (int(mmr) * 0.5)

def process_rewards(records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    
    for record in records:
        try:
            name = record[0]
            matches = record[1]
            mmr = record[2]
            
            bonus_rp = calculate_bonus(matches, mmr)
            print(f"Tuyển thủ {name} nhận được {bonus_rp} RP")
            
        except IndexError:
            print(f"Tuyển thủ {record[0]}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue
            
        except ValueError:
            print(f"Tuyển thủ {name}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue

    print("--- HOÀN TẤT ---")

process_rewards(player_records)
