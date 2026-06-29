# Test Coverage Analysis - RESTful Booker API

**Project:** RESTful Booker API Automation Framework  
**Tester:** Hồ Thị Diệu  
**Technology Stack:** Python • Pytest • Requests • Allure Report  
**Timeline:** Week 12 – Final Review & Integration Strategy  

---

## 1. Project Overview
Dự án này xây dựng một framework tự động hóa kiểm thử API cho hệ thống RESTful Booker bằng Python, Pytest và Requests. Framework được thiết kế theo hướng Data-Driven Testing, hỗ trợ kiểm thử các chức năng CRUD, sinh báo cáo HTML và Allure, đồng thời tích hợp Logging, JSON Schema Validation và Fixture để tăng khả năng tái sử dụng.

---

## 2. Scope

| Module | Description |
| :--- | :--- |
| **Authentication** | Xác thực tài khoản và lấy Token phục vụ các API yêu cầu phân quyền. |
| **Create Booking** | Tạo mới thông tin đặt phòng. |
| **Get Booking** | Truy xuất thông tin booking theo ID. |
| **Update Booking** | Cập nhật một phần thông tin booking. |
| **Delete Booking** | Xóa booking khỏi hệ thống. |

---

## 3. Framework Architecture
Luồng vận hành của Framework được tổ chức theo kiến trúc sau:
`Tests ──> BookingClient ──> Requests ──> RESTful Booker API ──> Response ──> Assertions ──> Logger ──> Allure Report`

---

## 4. Test Coverage Matrix

| Module | TC ID | Scenario | Type | Manual | Automation Coverage |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Authentication** | TC01 | Login thành công với tài khoản hợp lệ | Positive | ✔ | 100% |
| | TC02 | Login thất bại khi sai password | Negative | ✔ | |
| **Create Booking** | TC03 | Create booking với đầy đủ thông tin hợp lệ | Positive | ✔ | 100% |
| | TC04 | Create booking khi không truyền additionalneeds | Positive | ✔ | |
| | TC05 | Kiểm tra giá trị biên với totalprice = 0 | Boundary | ✔ | |
| | TC06 | Chặn lỗi khi trường firstname bị bỏ rỗng | Negative | ✔ | |
| **Get Booking** | TC07 | Get thông tin booking hợp lệ bằng ID | Positive | ✔ | 100% |
| | TC08 | Verify dữ liệu bốc về trùng khớp với lúc Create | Positive | ✔ | |
| | TC09 | Get booking với ID không tồn tại trên hệ thống | Negative | ✔ | |
| **Schema Validate**| TC10 | Verify cấu trúc JSON Schema response (TC03/TC07) | Positive | ✔ | 100% |
| **Update Booking** | TC11 | Update trường lastname thành công (PUT) | Positive | ✔ | 100% |
| | TC12 | Update nhiều trường thông tin cùng lúc (PUT) | Positive | ✔ | |
| | TC13 | Chặn cập nhật khi dùng Token giả | Negative | ✔ | |
| **Delete Booking** | TC14 | Delete booking thành công với token | Positive | ✔ | 100% |
| | TC15 | Verify lại ID booking đã xóa nhận về lỗi 404 | Positive | ✔ | |

---

## 5. Manual + Automation Strategy
* **Manual Testing:** Được sử dụng ở giai đoạn đầu để tìm hiểu nghiệp vụ (Business Behavior), khám phá hệ thống và thiết lập các kịch bản kiểm thử (Scenarios) cơ sở trên Postman.
* **Automation Testing (Pytest):** Áp dụng cho các kịch bản kiểm thử hồi quy ổn định (Stable Regression Scenarios). Giúp chạy lặp đi lặp lại 15 test cases chỉ trong vài giây, tự động hóa việc xác thực cấu hình dữ liệu lớn mà không tốn sức người.

---

## 6. Framework Features
Bộ Framework của dự án đáp ứng đầy đủ các tiêu chuẩn kỹ thuật nâng cao bao gồm:
* **Data-Driven Testing (JSON):** Tách biệt hoàn toàn dữ liệu test ra file `test_data.json`.
* **Fixtures Setup/Teardown:** Quản lý vòng đời chạy test, cấu hình URL và Token dùng chung một cách thông minh qua `conftest.py`.
* **BookingClient Pattern:** Tách biệt tầng gọi API và tầng assert dữ liệu (tương tự POM của UI).
* **Advanced Logging:** Ghi nhật ký tường tận quá trình gửi Request và nhận Response hỗ trợ đắc lực khi Debug lỗi.
* **Hook & Reporting:** Tích hợp sinh báo cáo trực quan sinh động bằng **Allure Report** và **HTML Report**.
* **JSON Schema Validation:** Tự động kiểm tra định dạng kiểu dữ liệu đầu ra đạt độ chính xác 100%.

---

## 7. Coverage Summary
* **Total Endpoints Covered:** 5 / 5 Endpoints cốt lõi.
* **Automated Test Cases:** 15 Test cases hoàn chỉnh (đã bao gồm Validation).
* **Endpoint Coverage Rate:** 100%
* **Regression Coverage:** 100% (Bao phủ toàn diện các luồng từ lý tưởng đến bắt lỗi hệ thống).

---

## 8. Conclusion
Framework này cung cấp một giải pháp tự động hóa kiểm thử API có khả năng tái sử dụng cao, kiến trúc phân lớp rõ ràng, hệ thống log và report tường minh.