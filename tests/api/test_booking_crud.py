import requests
from jsonschema import validate
import urllib3

# Tắt cảnh báo SSL khi sử dụng verify=False trong môi trường test
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://restful-booker.herokuapp.com"


def test_booking():

    print("\n===== LOGIN =====")

    # Chuẩn bị tài khoản hợp lệ để lấy token phục vụ các API cần xác thực
    body_login = {
        "username": "admin",
        "password": "password123"
    }

    # Đăng nhập hệ thống và nhận token
    response_login = requests.post(
        f"{BASE_URL}/auth",
        json=body_login,
        verify=False
    )

    # Xác nhận đăng nhập thành công
    assert response_login.status_code == 200

    print(f"Login Status: {response_login.status_code}")

    # Lưu token để sử dụng cho Update/Delete Booking
    token_login = response_login.json()["token"]

    print("\n===== CREATE BOOKING =====")

    # Header xác thực cho các API yêu cầu quyền chỉnh sửa dữ liệu
    header = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token_login}"
    }

    # Tạo dữ liệu booking mới phục vụ luồng CRUD
    body_booking = {
        "firstname": "Diệu",
        "lastname": "Hồ",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-06-01",
            "checkout": "2026-06-15"
        },
        "additionalneeds": "Học Automation"
    }

    # Tạo booking mới trên hệ thống
    response_create_booking = requests.post(
        f"{BASE_URL}/booking",
        json=body_booking,
        verify=False
    )

    # Xác nhận booking được tạo thành công
    assert response_create_booking.status_code == 200

    print(f"Create Status: {response_create_booking.status_code}")

    create_data = response_create_booking.json()

    # Lưu booking_id để sử dụng cho các bước Read / Update / Delete
    booking_id = create_data["bookingid"]

    # Verify dữ liệu trả về đúng với dữ liệu đã gửi lên
    assert create_data["booking"]["firstname"] == "Diệu"
    assert create_data["booking"]["lastname"] == "Hồ"
    assert create_data["booking"]["totalprice"] == 1000

    print("Create Data Validation Passed")

    print("\n===== READ BOOKING =====")

    # Lấy thông tin booking vừa tạo để phục vụ kiểm tra dữ liệu
    response_read = requests.get(
        f"{BASE_URL}/booking/{booking_id}",
        verify=False
    )

    # Xác nhận hệ thống trả về booking thành công
    assert response_read.status_code == 200

    print(f"Read Status: {response_read.status_code}")

    data_booking = response_read.json()

    # Verify dữ liệu đọc được khớp với dữ liệu đã tạo
    assert data_booking["firstname"] == "Diệu"
    assert data_booking["lastname"] == "Hồ"

    print("Read Data Validation Passed")

    print("\n===== VALIDATE JSON SCHEMA =====")

    # Định nghĩa cấu trúc dữ liệu mong đợi từ API Get Booking
    data_booking_type = {
        "type": "object",

        "properties": {

            "firstname": {
                "type": "string"
            },

            "lastname": {
                "type": "string"
            },

            "totalprice": {
                "type": "number"
            },

            "depositpaid": {
                "type": "boolean"
            },

            # Verify object bookingdates tồn tại
            # và chứa đầy đủ ngày checkin / checkout
            "bookingdates": {

                "type": "object",

                "properties": {

                    "checkin": {
                        "type": "string"
                    },

                    "checkout": {
                        "type": "string"
                    }
                },

                "required": [
                    "checkin",
                    "checkout"
                ]
            },

            "additionalneeds": {
                "type": "string"
            }
        },

        # Các field bắt buộc phải tồn tại trong response
        "required": [
            "firstname",
            "lastname",
            "totalprice",
            "depositpaid",
            "bookingdates"
        ]
    }

    # Xác nhận response đúng schema đã định nghĩa
    validate(
        instance=data_booking,
        schema=data_booking_type
    )

    print("Schema Validation Passed")

    print("\n===== UPDATE BOOKING =====")

    # Thay đổi họ của khách hàng để kiểm tra chức năng cập nhật
    body_change_name = {
        "lastname": "Thị"
    }

    # Cập nhật dữ liệu booking bằng token hợp lệ
    response_update = requests.patch(
        f"{BASE_URL}/booking/{booking_id}",
        json=body_change_name,
        headers=header,
        verify=False
    )

    # Xác nhận cập nhật thành công
    assert response_update.status_code == 200

    print(f"Update Status: {response_update.status_code}")

    # Verify dữ liệu được cập nhật trong response
    assert response_update.json()["lastname"] == "Thị"

    # Gọi lại API Get Booking để xác nhận dữ liệu thực sự được lưu trên hệ thống
    response_verify_update = requests.get(
        f"{BASE_URL}/booking/{booking_id}",
        verify=False
    )

    assert response_verify_update.status_code == 200
    assert response_verify_update.json()["lastname"] == "Thị"

    print("Update Validation Passed")

    print("\n===== NEGATIVE TEST =====")

    # Sử dụng token giả để kiểm tra cơ chế phân quyền
    wrong_header = {
        "Cookie": "token=abcxyz"
    }

    response_negative = requests.patch(
        f"{BASE_URL}/booking/{booking_id}",
        json={"lastname": "Hack"},
        headers=wrong_header,
        verify=False
    )

    # Hệ thống phải từ chối request không hợp lệ
    assert response_negative.status_code in [401, 403]

    print(
        f"Negative Test Passed - Status: "
        f"{response_negative.status_code}"
    )

    print("\n===== DELETE BOOKING =====")

    # Xóa booking đã tạo để dọn dữ liệu test
    response_delete = requests.delete(
        f"{BASE_URL}/booking/{booking_id}",
        headers=header,
        verify=False
    )

    # Restful-Booker trả về 201 khi xóa thành công
    assert response_delete.status_code == 201

    print(f"Delete Status: {response_delete.status_code}")

    # Xác nhận booking không còn tồn tại sau khi xóa
    response_verify_delete = requests.get(
        f"{BASE_URL}/booking/{booking_id}",
        verify=False
    )

    assert response_verify_delete.status_code == 404

    print("Delete Validation Passed")

    print("\n✅ HOÀN THÀNH TEST LOGIN & CRUD API")


test_booking()