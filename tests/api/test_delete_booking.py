import pytest
import allure

from utils.file_utils import read_json_file

ALL_DATA = read_json_file(
    "data/booking_data.json"
)

DELETE_DATA = ALL_DATA["delete_booking"]


@allure.epic("Restful Booker API")
@allure.feature("Delete Booking")
@allure.story("Delete Booking API")
@pytest.mark.api
class TestDeleteBooking:

    @allure.title("TC14 - Delete booking successfully")
    @allure.description(
        "Verify user can delete an existing booking successfully."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "test_data",
        [
            DELETE_DATA["tc14_delete_success"]
        ],
        ids=[
            "TC14-Delete-Success"
        ]
    )
    def test_delete_booking_success(
        self,
        booking_client,
        booking_id,
        headers,
        test_data
    ):

        with allure.step("Send Delete Booking Request"):

            response = booking_client.delete_booking(
                booking_id,
                headers
            )

        allure.attach(
            str({
                "booking_id": booking_id
            }),
            name="Request",
            attachment_type=allure.attachment_type.JSON
        )
        allure.attach(
            response.text,
            name="Response",
            attachment_type=allure.attachment_type.TEXT
        )

        with allure.step("Verify Status Code"):

            assert response.status_code == test_data["expected_delete_status"]


    @allure.title("TC15 - Verify deleted booking cannot be retrieved")
    @allure.description(
        "Verify deleted booking returns 404 when requesting Get Booking."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "test_data",
        [
            DELETE_DATA["tc15_verify_deleted"]
        ],
        ids=[
            "TC15-Verify-Deleted"
        ]
    )
    def test_deleted_booking_not_found(
        self,
        booking_client,
        booking_id,
        headers,
        test_data
    ):

        with allure.step("Delete Existing Booking"):

            delete_response = booking_client.delete_booking(
                booking_id,
                headers
            )

        allure.attach(
            str({
                "booking_id": booking_id
            }),
            name="Delete Request",
            attachment_type=allure.attachment_type.JSON
        )

        allure.attach(
            delete_response.text,
            name="Delete Response",
            attachment_type=allure.attachment_type.TEXT
        )
        with allure.step("Send Get Booking Request"):

            get_response = booking_client.get_booking(
                booking_id
            )
        allure.attach(
            get_response.text,
            name="Get Response",
            attachment_type=allure.attachment_type.TEXT
        )

        with allure.step("Verify Booking Not Found"):

            assert get_response.status_code == \
                test_data["expected_get_status"]