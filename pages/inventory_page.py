# Import công cụ By để định vị các phần tử (UI Element) trên trang web
from selenium.webdriver.common.by import By
# Import thư viện Select để xử lý tương tác với các thẻ dropdown menu truyền thống
from selenium.webdriver.support.ui import Select
# Import các điều kiện chờ có sẵn của Selenium để bắt trạng thái hiển thị của thẻ dropdown
from selenium.webdriver.support import expected_conditions as EC
# Import lớp cha BasePage để kế thừa các hàm thao tác cơ bản
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    InventoryPage là lớp đối tượng trang (Page Object) quản lý giao diện Danh sách sản phẩm.
    Mục đích:
    - Định vị tất cả các phần tử (Locators) thuộc kho hàng và hệ thống menu điều hướng.
    - Định nghĩa các hành động (Actions) lọc giá, thêm vào giỏ hàng và đăng xuất.
    - Kế thừa BasePage để sử dụng lại các hàm tương tác chung.
    """

    def __init__(self, driver):
        # Kích hoạt hàm khởi tạo của lớp cha BasePage để nạp driver và wait
        super().__init__(driver)

        # Định vị tiêu đề chính của trang sản phẩm (chữ "Products")
        self.page_title = (By.CLASS_NAME, "title")
        # Định vị menu dropdown dùng để sắp xếp/lọc sản phẩm
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        # Định vị nút bấm Thêm sản phẩm Sauce Labs Backpack vào giỏ hàng
        self.add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
        # Định vị biểu tượng vòng tròn đỏ hiển thị số lượng sản phẩm trên icon giỏ hàng
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        # Định vị icon giỏ hàng dùng để nhấn chuyển trang xem giỏ hàng
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        # Định vị nút bấm mở thanh menu ẩn bên góc trái màn hình (Burger Menu)
        self.menu_btn = (By.ID, "react-burger-menu-btn")
        # Định vị liên kết Đăng xuất (Logout) nằm bên trong thanh menu ẩn
        self.logout_btn = (By.ID, "logout_sidebar_link")

    # Khởi tạo hàm kiểm tra trang danh sách sản phẩm có hiển thị hay không
    def is_inventory_page_displayed(self):
        # Gọi hàm kiểm tra hiển thị từ BasePage để Verify trạng thái đăng nhập thành công
        return self.is_element_visible(self.page_title)

    # Khởi tạo hàm Sắp xếp sản phẩm theo tiêu chí Giá từ thấp đến cao
    def sort_price_low_to_high(self):
        # Đợi cho thanh dropdown sort xuất hiện trong cấu trúc DOM của trang web
        dropdown_element = self.wait.until(EC.presence_of_element_located(self.sort_dropdown))
        # Sử dụng thư viện Select để chọn giá trị "lohi" (Price - Low to High)
        Select(dropdown_element).select_by_value("lohi")

    # Khởi tạo hàm Click vào nút Add to cart để chọn mua sản phẩm
    def add_product_to_cart(self):
        # Gọi hàm click từ BasePage để thêm món hàng được chỉ định vào giỏ
        self.click_element(self.add_to_cart_btn)

    # Khởi tạo hàm Click vào icon Giỏ hàng để chuyển sang giao diện xem giỏ hàng
    def go_to_cart(self):
        # Gọi hàm click từ BasePage để chuyển hướng màn hình
        self.click_element(self.cart_icon)

    # Khởi tạo hàm Thực hiện đăng xuất tài khoản khỏi hệ thống
    def logout(self):
        # Gọi hàm click từ BasePage để mở rộng thanh menu ẩn bên trái
        self.click_element(self.menu_btn)
        # Gọi hàm click từ BasePage vào link Logout để thoát phiên làm việc
        self.click_element(self.logout_btn)

    # Khởi tạo hàm lấy số lượng hiển thị trên biểu tượng giỏ hàng
    def get_cart_badge(self):
        # Gọi hàm lấy text từ BasePage và trả về kết quả để file Test thực hiện Assert
        return self.get_text(self.cart_badge)
