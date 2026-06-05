# Import công cụ By để định vị các phần tử (UI Element) trên trang web
from selenium.webdriver.common.by import By
# Import lớp cha BasePage để kế thừa các hàm thao tác cơ bản
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    LoginPage là lớp đối tượng trang (Page Object) quản lý giao diện Đăng nhập hệ thống.
    Mục đích:
    - Định vị các phần tử (Locators) như ô tài khoản, mật khẩu, nút đăng nhập và thông báo lỗi.
    - Định nghĩa các hành động (Actions) mở trang web và thực hiện đăng nhập.
    - Kế thừa BasePage để sử dụng lại các hàm tương tác chung.
    """
    
    def __init__(self, driver):
        # Kích hoạt hàm khởi tạo của lớp cha BasePage để nạp driver và wait
        super().__init__(driver)
        # Lưu trữ địa chỉ URL trực tiếp của trang chủ SauceDemo
        self.url = "https://www.saucedemo.com/"
        # Định vị ô nhập tên tài khoản (Username Input Field)
        self.username_input = (By.ID, "user-name")
        # Định vị ô nhập mật khẩu (Password Input Field)
        self.password_input = (By.ID, "password")
        # Định vị nút bấm Đăng nhập (Login Button)
        self.login_btn = (By.ID, "login-button")
        # Định vị vùng hiển thị thông báo lỗi khi đăng nhập thất bại
        self.error_message = (By.CSS_SELECTOR, 'h3[data-test="error"]')

    # Khởi tạo hàm Điều hướng trình duyệt mở trang đăng nhập
    def open_page(self):
        # Gọi lệnh điều hướng driver truy cập vào địa chỉ URL của trang chủ
        self.driver.get(self.url)

    # Khởi tạo hàm Thực hiện đăng nhập vào hệ thống bằng tài khoản và mật khẩu
    def login(self, username, password):
        # Gọi hàm nhập văn bản từ BasePage để điền thông tin tài khoản mẫu
        self.input_text(self.username_input, username)
        # Gọi hàm nhập văn bản từ BasePage để điền thông tin mật khẩu mẫu
        self.input_text(self.password_input, password)
        # Gọi hàm click từ BasePage để nhấn nút Login gửi yêu cầu đăng nhập
        self.click_element(self.login_btn)

    # Khởi tạo hàm lấy nội dung thông báo lỗi khi đăng nhập không thành công
    def get_error_message(self):
        # Gọi hàm lấy text từ BasePage và trả về chuỗi văn bản để file Test thực hiện Assert
        return self.get_text(self.error_message)
    
    # Khởi tạo hàm kiểm tra nút bấm Đăng nhập có đang hiển thị hay không
    def is_login_button_displayed(self):
        # Gọi hàm kiểm tra hiển thị từ BasePage để Verify trạng thái sau khi User nhấn Đăng xuất
        return self.is_element_visible(self.login_btn)
