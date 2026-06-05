# 🛒 SauceDemo E2E Automation Testing (POM)

Dự án Automation Testing cho website [SauceDemo](https://www.saucedemo.com/) sử dụng Selenium WebDriver và Page Object Model (POM).

## 🚀 Tính năng nổi bật
* **Cấu trúc POM chuẩn:** Tách biệt hoàn toàn phần giao diện (Pages), phần kiểm thử (Tests), dữ liệu (Data) và công cụ hỗ trợ (Utils).
* **Data-Driven Testing (DDT):** Đọc dữ liệu test (username, password, checkout info) từ file `.json` để dễ quản lý và bảo trì.
* **Xử lý sự cố môi trường (Environment Issues):** Tùy chỉnh `DriverFactory` (ChromeOptions) để tắt hoàn toàn các pop-up hỏi lưu mật khẩu, cảnh báo rò rỉ dữ liệu và thông báo điều khiển tự động của Chrome, giúp script chạy ổn định 100%.
* **Tự động chụp màn hình:** Tích hợp `try...except`, tự động chụp ảnh màn hình lưu vào `/results/screenshots/` nếu testcase bị fail.

## 📁 Cấu trúc thư mục
- `pages/`: Chứa các Page Objects kế thừa từ `BasePage`.
- `tests/`: Chứa kịch bản kiểm thử (Login, Cart, Checkout).
- `data/`: Chứa file test data JSON.
- `utils/`: Khởi tạo Chrome Driver và các hàm xử lý file.

## 🛠️ Hướng dẫn cài đặt & Chạy Test
1. Cài đặt các thư viện cần thiết: 
   ```bash
   pip install -r requirements.txt
