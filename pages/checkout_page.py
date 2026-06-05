# Import công cụ By để định vị các phần tử (UI Element) trên trang web
from selenium.webdriver.common.by import By
# Import lớp cha BasePage để kế thừa các hàm thao tác cơ bản
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """
    CheckoutPage là lớp đối tượng trang (Page Object) quản lý giao diện Thanh toán.
    Mục đích:
    - Định vị tất cả các phần tử (Locators) thuộc luồng điền thông tin và xác nhận đơn hàng.
    - Định nghĩa các hành động (Actions) nhập liệu, bấm nút trong quá trình mua hàng.
    - Kế thừa BasePage để sử dụng lại các hàm tương tác chung.
    """

    def __init__(self, driver):
        # Kích hoạt hàm khởi tạo của lớp cha BasePage để nạp driver và wait
        super().__init__(driver)
        # Định vị ô nhập liệu Tên (First Name)
        self.first_name = (By.ID, "first-name")
        # Định vị ô nhập liệu Họ và tên đệm (Last Name)
        self.last_name = (By.ID, "last-name")
        # Định vị ô nhập liệu Mã bưu điện (Zip/Postal Code)
        self.zip_code = (By.ID, "postal-code")
        # Định vị nút bấm Tiếp tục (Continue) để chuyển sang trang soát xét đơn hàng
        self.continue_btn = (By.ID, "continue")
        # Định vị nút bấm Hoàn tất (Finish) để chốt đơn mua hàng
        self.finish_btn = (By.ID, "finish")
        # Định vị phần tử hiển thị thông báo đặt hàng thành công (Success Message Header)
        self.success_message = (By.CLASS_NAME, "complete-header")
        # Định vị nút bấm Quay lại trang chủ (Back Home) sau khi mua hàng xong
        self.back_home_btn = (By.ID, "back-to-products")
    
    # Khởi tạo hàm nhập thông tin cá nhân vào form thanh toán
    def fill_checkout_information(self, first_name, last_name, zip_code):
        # Gọi hàm nhập văn bản từ BasePage để điền thông tin Tên khách hàng
        self.input_text(self.first_name, first_name)
        # Gọi hàm nhập văn bản từ BasePage để điền thông tin Họ khách hàng
        self.input_text(self.last_name, last_name)
        # Gọi hàm nhập văn bản từ BasePage để điền thông tin Mã bưu điện
        self.input_text(self.zip_code, zip_code)

    # Khởi tạo hàm Click vào nút Continue để tiếp tục luồng thanh toán
    def click_continue(self):
        # Gọi hàm click từ BasePage để xác nhận thông tin form và chuyển trang
        self.click_element(self.continue_btn)

    # Khởi tạo hàm Click vào nút Finish để hoàn tất đơn hàng
    def click_finish(self):
        # Gọi hàm click từ BasePage để gửi lệnh chốt đơn lên hệ thống
        self.click_element(self.finish_btn)
    
    # Khởi tạo hàm lấy nội dung thông báo đặt hàng thành công
    def get_success_message(self):
        # Gọi hàm lấy text từ BasePage và trả về kết quả để file Test thực hiện Assert
        return self.get_text(self.success_message)

    # Khởi tạo hàm Click vào nút Back Home để quay về trang danh sách sản phẩm
    def back_to_home(self):
        # Gọi hàm click từ BasePage để điều hướng trình duyệt quay lại kho hàng
        self.click_element(self.back_home_btn)
