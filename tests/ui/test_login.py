# Import thư viện hệ thống để xử lý đường dẫn project
import sys
import os

# Thêm thư mục gốc của project vào PYTHONPATH
# để có thể import các package pages/, utils/, data/
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../.."
        )
    )
)
# Import các Page Object
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
# Import Driver Factory để khởi tạo Chrome driver
from utils.driver_factory import DriverFactory
# Import hàm đọc file từ utils
from utils.file_utils import read_json_file
# ĐỌC DATA TỪ FILE JSON
# Lấy toàn bộ data từ file json
ALL_DATA = read_json_file("data/test_data.json")
# Trỏ thẳng vào cục data dùng cho login
LOGIN_DATA = ALL_DATA["login_data"]

# Khởi tạo hàm kiểm thử luồng đăng nhập thành công
def test_login_success():
    """
    Login Success Flow
    Flow:
    Open Login Page
    → Login with valid credentials
    → Verify user is redirected to Inventory Page
    """
    # Khởi tạo Chrome Browser
    driver = DriverFactory.get_chrome_driver()

    try:
        # Khởi tạo các Page Object 
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        print("=== CHẠY TEST LUỒNG ĐĂNG NHẬP ===")
        print("Đang đăng nhập với dữ liệu đúng...")
        # 1: Truy cập trang Login
        login_page.open_page()
        # 2. Đăng nhập bằng tài khoản hợp lệ
        login_page.login(
            LOGIN_DATA["valid_user"]["username"],
            LOGIN_DATA["valid_user"]["password"]
        )

        # 3. Verify người dùng được điều hướng tới trang Products sau khi đăng nhập thành công
        assert inventory_page.is_inventory_page_displayed()
        print ("PASS: Đăng nhập thành công")

    except Exception as e:
        # Chụp màn hình khi testcase fail
        driver.save_screenshot("results/screenshots/login_with_valid_data_fail.png")
        print (f"Fail: Lỗi khi đăng nhập với dữ liệu đúng: {e}")
    
    finally:
        driver.quit()

# Khởi tạo hàm kiểm thử luồng đăng nhập thất bại với dữ liệu sai
def test_login_fail():
    """
    Login Failed Flow

    Flow:
    Open Login Page
    → Login with invalid password
    → Verify error message is displayed
    """
    driver = DriverFactory.get_chrome_driver()

    try:
        # Khởi tạo Login Page
        login_page = LoginPage(driver)

        print("=== CHẠY TEST LUỒNG ĐĂNG NHẬP VỚI WRONG DATA ===")
        print("Đang đăng nhập với dữ liệu sai...")
        
        # 1. Truy cập trang Login
        login_page.open_page()

        # 2. Đăng nhập bằng mật khẩu không hợp lệ
        login_page.login(
            LOGIN_DATA["invalid_user"]["username"],
            LOGIN_DATA["invalid_user"]["password"]
        )

        # 3. Verify hệ thống hiển thị thông báo lỗi đăng nhập
        assert "Username and password do not match " in login_page.get_error_message()
        print ("PASS: Đăng nhập không thành công với dữ liệu sai")

    except Exception as e:
        # Chụp màn hình khi testcase fail
        driver.save_screenshot("results/screenshots/login_with_invalid_data_fail.png")
        print (f"Fail: Lỗi khi đăng nhập với dữ liệu sai: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_login_success()
    test_login_fail()


