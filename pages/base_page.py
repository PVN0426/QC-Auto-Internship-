# Import WebDriverWait để thực hiện Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
# Import các điều kiện chờ có sẵn của Selenium
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    BasePage là lớp cha dùng chung cho tất cả các Page Object.
    Mục đích:
    - Chứa các hàm thao tác cơ bản với UI.
    - Tránh lặp code giữa các page.
    - Hỗ trợ áp dụng mô hình POM (Page Object Model).

    Các page như:
    LoginPage
    InventoryPage
    CartPage
    CheckoutPage

    sẽ kế thừa từ BasePage để sử dụng lại các hàm chung.
    """

    def __init__(self, driver):
        # Khởi tạo WebDriver
        self.driver = driver
        # Khởi tạo Explicit Wait với timeout 10 giây
        self.wait = WebDriverWait(self.driver, 10)

    #  khởi tạo hàm Click vào một element
    def click_element(self, locator):
        # Chờ element có thể click được     
        element = self.wait.until( EC.element_to_be_clickable(locator))
        # Thực hiện click
        element.click()

    # Khởi tạo hàm nhập dữ liệu vào textbox
    def input_text(self, locator, text):
        print(f"Đang nhập {text} vào {locator}")
        # Chờ Textbox hiển thị trên màn hình
        element = self.wait.until(EC.visibility_of_element_located(locator))
        # Xóa sạch chuỗi ký tự đang có sẵn trong ô nhập liệu
        element.clear()
        # Truyền Test Data vào Textbox
        element.send_keys(text)

    # Khởi tạo hàm lấy nội dung text của element
    def get_text(self, locator):
        # Chờ phần tử chứa văn bản cần kiểm tra hiển thị rõ ràng trên UI
        element = self.wait.until(EC.visibility_of_element_located(locator))
        # Trả về chuỗi Text để file Test thực hiện so sánh kết quả
        return element.text

    # Khởi tạo hàm kiểm tra element có hiển thị hay không
    def is_element_visible(self, locator):
        try:
            # Thực hiện Wait ngầm trong khoảng Timeout quy định
            self.wait.until(EC.visibility_of_element_located(locator))
            return True # Kết quả Verify: Element có hiển thị

        except:
            return False # Kết quả Verify: Element không hiển thị

    # Khởi tạo hàm lấy URL hiện tại của trình duyệt
    def get_current_url(self):
        return self.driver.current_url

    # Khởi tạo hàm Đếm số lượng element theo locator
    def get_elements_count(self, locator):
        # Tìm kiếm tập hợp các phần tử 
        elements = self.driver.find_elements(*locator)
        return len(elements) #Trả về tổng số lượng đếm được dưới dạng số nguyên