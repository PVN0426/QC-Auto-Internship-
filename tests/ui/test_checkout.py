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
import time
# Import các Page Object
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
# Import Driver Factory để khởi tạo Chrome driver
from utils.driver_factory import DriverFactory
# Import hàm đọc file từ utils
from utils.file_utils import read_json_file
# ĐỌC DATA TỪ FILE JSON
# Lấy toàn bộ data từ file json
ALL_DATA = read_json_file("data/test_data.json")
# Trỏ thẳng vào cục data dùng cho login
LOGIN_DATA = ALL_DATA["login_data"]
CHECKOUT_DATA = ALL_DATA["checkout_data"]

#Khởi tạo hàm kiểm thử luồng thanh toán
def test_luong_thanh_toan():
    """
    E2E Checkout Flow
    Flow:
    Login → Add Product → Cart → Checkout → Complete Order → Back Home → Logout
    """
    # Khởi tạo Chrome Browser
    driver = DriverFactory.get_chrome_driver()
    
    try:
        # Khởi tạo các Page Object
        login_pg = LoginPage(driver)
        inventory_pg = InventoryPage(driver)
        cart_pg = CartPage(driver)
        checkout_pg = CheckoutPage(driver)

        print("=== CHẠY TEST LUỒNG THANH TOÁN (E2E) ===")
        # 1. Login bằng tài khoản hợp lệ
        login_pg.open_page()
        login_pg.login(LOGIN_DATA["valid_user"]["username"], LOGIN_DATA["valid_user"]["password"])
        
        # 2. Thêm sản phẩm vào giỏ hàng
        inventory_pg.add_product_to_cart()
        # Verify badge hiển thị 1 sản phẩm
        assert inventory_pg.get_cart_badge() == "1"
        # Điều hướng tới trang Cart
        inventory_pg.go_to_cart()
        # Verify Cart chứa đúng 1 sản phẩm
        assert cart_pg.get_total_products_in_cart() == 1
        # 3. Clicking Checkout
        cart_pg.click_checkout()
        
        # 4. Nhập thông tin khách hàng
        checkout_pg.fill_checkout_information(CHECKOUT_DATA["first_name"], CHECKOUT_DATA["last_name"], CHECKOUT_DATA["zip_code"])
        #Chuyển sang màn hình Checkout Overview
        checkout_pg.click_continue()

        # 5. Hoàn tất đơn hàng
        checkout_pg.click_finish()
        #Verify thông báo mua hàng thành công
        verify_chekout = checkout_pg.get_success_message() 
        assert "Thank you for your order!" in verify_chekout
        print("PASS: Mua hàng thành công!")

        # 6.Quay về trang Inventory
        checkout_pg.back_to_home() 
        
        # 7. Logout
        inventory_pg.logout()
        # Verify đã quay về trang Login
        assert login_pg.get_current_url() == "https://www.saucedemo.com/"
        # Verify nút Login hiển thị
        assert login_pg.is_login_button_displayed() is True
        print("PASS: Đăng xuất thành công!")

    except Exception as e:
        # Chụp màn hình khi testcase fail
        driver.save_screenshot("results/screenshots/chekout_fail.png")
        print(f"FAIL: Lỗi: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_luong_thanh_toan()


