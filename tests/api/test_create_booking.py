import pytest
import allure
from jsonschema import validate

from schemas.booking_schema import BOOKING_SCHEMA
from utils.file_utils import read_json_file

ALL_DATA = read_json_file(
    "data/booking_data.json"
)

CREATE_DATA = ALL_DATA["create_booking"]


@allure.epic("Restful Booker API")
@allure.feature("Create Booking")
@allure.story("Create Booking API")
@pytest.mark.api
class TestCreateBooking:

    @allure.title("Verify Create Booking API")
    @allure.description(
        "Verify create booking API with different booking data."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "test_data",
        [
            CREATE_DATA["tc03_valid_booking"],
            CREATE_DATA["tc04_missing_additionalneeds"],
            CREATE_DATA["tc05_price_boundary_zero"],
            CREATE_DATA["tc06_empty_firstname"]
        ],
        ids=[
            "TC03-Valid-Booking",
            "TC04-Missing-AdditionalNeeds",
            "TC05-Price-Zero",
            "TC06-Empty-Firstname"
        ]
    )
    def test_create_booking(
        self,
        booking_client,
        test_data
    ):

        with allure.step("Send Create Booking Request"):
            response = booking_client.create_booking(
                test_data["payload"]
            )

        allure.attach(
            str(test_data["payload"]),
            "Request",
            allure.attachment_type.JSON
        )

        allure.attach(
            str(response.json()),
            "Response",
            allure.attachment_type.JSON
        )

        with allure.step("Verify Status Code"):
            assert response.status_code == \
                test_data["expected_status"]

        with allure.step("Verify Response Body"):
            response_data = response.json()

            assert "bookingid" in response_data
            assert "booking" in response_data

        with allure.step("Validate Booking Schema"):
            validate(
                instance=response_data["booking"],
                schema=BOOKING_SCHEMA
            )