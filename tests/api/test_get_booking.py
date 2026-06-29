import pytest
import allure
from jsonschema import validate

from schemas.booking_schema import BOOKING_SCHEMA
from utils.file_utils import read_json_file

ALL_DATA = read_json_file(
    "data/booking_data.json"
)

GET_DATA = ALL_DATA["get_booking"]


@allure.epic("Restful Booker API")
@allure.feature("Get Booking")
@allure.story("Get Booking API")
@pytest.mark.api
class TestGetBooking:

    @allure.title("Verify Get Booking Successfully")
    @allure.description(
        "Verify user can get booking information successfully."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_get_booking_success(
        self,
        booking_client,
        booking_id
    ):

        with allure.step("Send Get Booking Request"):

            response = booking_client.get_booking(
                booking_id
            )

        allure.attach(
            str(booking_id),
            name="Booking ID",
            attachment_type=allure.attachment_type.TEXT
        )

        allure.attach(
            str(response.json()),
            name="Response",
            attachment_type=allure.attachment_type.JSON
        )

        with allure.step("Verify Status Code"):

            assert response.status_code == 200

        with allure.step("Verify Response Body"):

            response_data = response.json()

            assert "firstname" in response_data
            assert "lastname" in response_data
            assert "totalprice" in response_data

    @allure.title("Verify Get Booking Response Schema")
    @allure.description(
        "Verify Get Booking response matches booking schema."
    )
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_get_booking_response_structure(
        self,
        booking_client,
        booking_id
    ):

        with allure.step("Send Get Booking Request"):

            response = booking_client.get_booking(
                booking_id
            )

        allure.attach(
            str(response.json()),
            name="Response",
            attachment_type=allure.attachment_type.JSON
        )

        with allure.step("Verify Status Code"):

            assert response.status_code == 200

        with allure.step("Validate Booking Schema"):

            validate(
                instance=response.json(),
                schema=BOOKING_SCHEMA
            )

    @allure.title("Verify Get Booking With Invalid ID")
    @allure.description(
        "Verify API returns 404 when booking ID does not exist."
    )
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "test_data",
        [
            GET_DATA["tc09_invalid_id"]
        ],
        ids=[
            "TC09-Invalid-ID"
        ]
    )
    def test_get_booking_invalid_id(
        self,
        booking_client,
        test_data
    ):

        with allure.step("Send Get Booking Request"):

            response = booking_client.get_booking(
                test_data["booking_id"]
            )

        allure.attach(
            str(test_data),
            name="Request",
            attachment_type=allure.attachment_type.JSON
        )

        allure.attach(
            str(response.text),
            name="Response",
            attachment_type=allure.attachment_type.TEXT
        )

        with allure.step("Verify Status Code"):

            assert response.status_code == \
                test_data["expected_status"]