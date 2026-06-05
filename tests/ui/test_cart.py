# Import thư viện xử lý đường dẫn để Python nhận diện được cấu trúc project
import sys
import os

# Thêm thư mục gốc của project vào PYTHONPATH
# để có thể import các package như pages/, data/, utils/
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
from pages.cart_page import CartPage
# Import Driver Factory để khởi tạo Chrome Driver
from utils.driver_factory import DriverFactory
# Import hàm đọc file từ utils
from utils.file_utils import read_json_file
# ĐỌC DATA TỪ FILE JSON
# Lấy toàn bộ data từ file json
ALL_DATA = read_json_file("data/test_data.json")
# Trỏ thẳng vào cục data dùng cho login
LOGIN_DATA = ALL_DATA["login_data"]

# Khởi tạo hàm kiểm thử luồng thêm sản phẩm vào giỏ hàng
def test_add_product_to_cart():
    """
    Add Product To Cart Flow

    Flow:
    Login
    → Sort products by price (Low to High)
    → Add product to cart
    → Open Cart Page
    → Verify product is added successfully
    """
    # Khởi tạo trình duyệt Chrome
    driver = DriverFactory.get_chrome_driver()
    try:
        # Khởi tạo các Page Object
        login_pg = LoginPage(driver)
        inventory_pg = InventoryPage(driver)
        cart_pg = CartPage(driver)

        print("=== CHẠY TEST LUỒNG GIỎ HÀNG ===")
        # 1. Mở trang đăng nhập
        login_pg.open_page()
        print("Đang đăng nhập...")
        # 2. Đăng nhập bằng tài khoản hợp lệ
        login_pg.login(LOGIN_DATA["valid_user"]["username"],LOGIN_DATA["valid_user"]["password"])        
        
        # 3. Sắp xếp sản phẩm theo giá từ thấp đến cao
        inventory_pg.sort_price_low_to_high()

        # 4. Thêm sản phẩm vào giỏ hàng
        inventory_pg.add_product_to_cart() 
        # Verify badge trên icon Cart hiển thị 1
        assert inventory_pg.get_cart_badge() == "1"

        # 5. Điều hướng tới trang Cart
        inventory_pg.go_to_cart()
        # Verify giỏ hàng có đúng 1 sản phẩm
        assert cart_pg.get_total_products_in_cart() == 1
        print("PASS: Đã thành công thêm 1 sản phẩm vào giỏ hàng!")
    
    except Exception as e:
        driver.save_screenshot("results/screenshots/add_to_cart_fail.png")
        print(f"FAIL: Lỗi: {e}")
    
    finally:
        driver.quit()

# Khởi tạo hàm kiểm thử luồng xóa sản phẩm trong giỏ hàng
def test_remove_product_from_cart():
    """
    Remove Product From Cart Flow

    Flow:
    Login
    → Add product to cart
    → Open Cart Page
    → Remove product
    → Verify cart becomes empty
    """
    # Khởi tạo trình duyệt Chrome
    driver = DriverFactory.get_chrome_driver()

    try:
        # Khởi tạo các Page Object
        login_pg = LoginPage(driver)
        inventory_pg = InventoryPage(driver)
        cart_pg = CartPage(driver)
        
        print("=== CHẠY TEST REMOVE PRODUCT ===")
        # 1. Mở trang đăng nhập
        login_pg.open_page()
        print ("Đang đăng nhập")
        # 2. Đăng nhập bằng tài khoản hợp lệ
        login_pg.login(LOGIN_DATA["valid_user"]["username"],LOGIN_DATA["valid_user"]["password"])

        # 3. Thêm sản phẩm vào giỏ hàng
        print("Đang thêm sản phẩm vào giỏ hàng")
        inventory_pg.add_product_to_cart() 

        # 4. Điều hướng tới trang Cart
        inventory_pg.go_to_cart()
        # Verify giỏ hàng có ít nhất 1 sản phẩm
        assert cart_pg.get_total_products_in_cart() == 1, "Giỏ hàng chưa có sản phẩm nào"
        print("Đang xóa sản phẩm khỏi giỏ hàng")

        # 5. Xóa sản phẩm khỏi giỏ hàng
        cart_pg.remove_product()
        # Verify giỏ hàng không còn sản phẩm nào
        assert cart_pg.get_total_products_in_cart() == 0
        print("PASS: Xóa sản phẩm thành công!")

    except Exception as e:
        driver.save_screenshot("results/screenshots/remove_product_fail.png")
        print (f"Fail: Lỗi khi xóa sản phẩm: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_add_product_to_cart()
    test_remove_product_from_cart()


