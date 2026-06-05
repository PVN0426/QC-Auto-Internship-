
import json
import os

# Hàm ĐỌC file JSON
def read_json_file(file_path):
    # Dùng đường dẫn tuyệt đối để tránh lỗi không tìm thấy file
    absolute_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", file_path))
    with open(absolute_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

# Hàm GHI file JSON (Dùng để xuất Report kết quả)
def write_json_file(file_path, data):
    absolute_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", file_path))
    with open(absolute_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)