# Conftest chỉ chứa setup/teardown
import pytest
from utils.driver_factory import DriverFactory
from utils.api_client import BookingClient
import allure
from utils.screenshot import take_screenshot

@pytest.fixture(scope="function")
def driver():

    driver = DriverFactory.get_chrome_driver()

    yield driver

    driver.quit()

@pytest.fixture(scope="session")
def booking_client():

    return BookingClient()
    
@pytest.fixture(scope="session")
def token(booking_client):

    booking_client.logger.info("=== LOGIN START ===")
    response = booking_client.login(
        username="admin",
        password="password123"
    )

    print(response.status_code)

    print(response.text)

    return response.json()["token"]

@pytest.fixture(scope="session")
def headers(token):

    return {

        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }

@pytest.fixture(scope="function")
def booking_id(headers, booking_client):
    booking_client.logger.info("=== CREATE BOOKING START ===")
    payload = {
        "firstname": "Diệu",
        "lastname": "Hồ",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-06-01",
            "checkout": "2026-06-15"
        }
    }

    response = booking_client.create_booking(payload)

    assert response.status_code == 200

    booking_id = response.json()["bookingid"]

    yield booking_id

    verify = booking_client.get_booking(booking_id)

    if verify.status_code == 200:
        booking_client.logger.info(
            f"Cleanup booking {booking_id}"
        )
        booking_client.delete_booking(
            booking_id,
            headers
        )
    else:
        booking_client.logger.info(
            f"Booking {booking_id} already deleted."
        )

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            screenshot_path = take_screenshot(
                driver,
                item.name
            )

            with open(
                screenshot_path,
                "rb"
            ) as image:

                allure.attach(
                    image.read(),
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
# def pytest_runtest_makereport():

# def take_screenshot():

# def logger():