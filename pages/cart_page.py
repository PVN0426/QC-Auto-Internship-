# Import công cụ By để định vị các phần tử (UI Element) trên trang web
from selenium.webdriver.common.by import By
# Import lớp cha BasePage để kế thừa các hàm thao tác cơ bản
from pages.base_page import BasePage


class CartPage(BasePage):
    """
    CartPage là lớp đối tượng trang (Page Object) quản lý giao diện Giỏ hàng.
    Mục đích:
    - Định vị tất cả các phần tử (Locators) thuộc trang Giỏ hàng.
    - Định nghĩa các hành động (Actions) của User trên trang này.
    - Kế thừa BasePage để sử dụng lại các hàm tương tác chung.
    """

    def __init__(self, driver):
        # Kích hoạt hàm khởi tạo của lớp cha BasePage để nạp driver và wait
        super().__init__(driver)
        # Định vị nút bấm Tiến hành thanh toán (Checkout)
        self.checkout_btn = (By.ID, "checkout")
        # Định vị nút bấm Xóa sản phẩm khỏi giỏ hàng (Remove)
        self.remove_btn = (By.ID, "remove-sauce-labs-backpack")
        # Định vị nút bấm Tiếp tục mua sắm (Continue Shopping)
        self.continue_shopping_btn = (By.ID, "continue-shopping")
        # Định vị phần tử đại diện cho từng sản phẩm nằm trong giỏ hàng
        self.cart_item = (By.CLASS_NAME, "cart_item")
    
    # Khởi tạo hàm kiểm tra sản phẩm có hiển thị trong giỏ hàng hay không
    def is_product_displayed(self):
        # Gọi hàm kiểm tra hiển thị từ BasePage để Verify trạng thái sản phẩm
        return self.is_element_visible(self.cart_item)

    # Khởi tạo hàm Click vào nút Checkout để tiến hành thanh toán
    def click_checkout(self):
        # Gọi hàm click từ BasePage để chuyển sang trang điền thông tin thanh toán
        self.click_element(self.checkout_btn)

    # Khởi tạo hàm Click vào nút Tiếp tục mua sắm
    def continue_shopping(self):
        # Gọi hàm click từ BasePage để quay trở lại trang danh sách sản phẩm
        self.click_element(self.continue_shopping_btn)

    # Khởi tạo hàm Click vào nút Remove để xóa sản phẩm
    def remove_product(self):
        # Gọi hàm click từ BasePage để loại bỏ sản phẩm ra khỏi giỏ hàng
        self.click_element(self.remove_btn)
    
    # Khởi tạo hàm Đếm tổng số lượng sản phẩm đang có trong giỏ hàng
    def get_total_products_in_cart(self):
        # Gọi hàm đếm số lượng từ BasePage và trả về kết quả để file Test thực hiện Assert
        return self.get_elements_count(self.cart_item)
