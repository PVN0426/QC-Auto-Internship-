import pytest
import allure

from utils.file_utils import read_json_file

ALL_DATA = read_json_file(
    "data/booking_data.json"
)

UPDATE_DATA = ALL_DATA["update_booking"]


@allure.epic("Restful Booker API")
@allure.feature("Update Booking")
@allure.story("Update Booking API")
@pytest.mark.api
class TestUpdateBooking:

    @allure.title("Verify Update Lastname Successfully")
    @allure.description(
        "Verify user can update booking lastname successfully."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "test_data",
        [
            UPDATE_DATA["tc11_update_lastname"]
        ],
        ids=[
            "TC11-Update-Lastname"
        ]
    )
    def test_update_lastname(
        self,
        booking_client,
        booking_id,
        headers,
        test_data
    ):

        with allure.step("Send Update Booking Request"):

            response = booking_client.update_booking(
                booking_id,
                test_data["payload"],
                headers
            )

        allure.attach(
            str(test_data["payload"]),
            name="Request",
            attachment_type=allure.attachment_type.JSON
        )

        allure.attach(
            str(response.json()),
            name="Response",
            attachment_type=allure.attachment_type.JSON
        )

        with allure.step("Verify Status Code"):

            assert response.status_code == \
                test_data["expected_status"]

        with allure.step("Verify Updated Lastname"):

            response_data = response.json()

            assert response_data["lastname"] == \
                test_data["payload"]["lastname"]

        with allure.step("Verify Data Saved Successfully"):

            verify_response = booking_client.get_booking(
                booking_id
            )

            verify_data = verify_response.json()

            assert verify_data["lastname"] == \
                test_data["payload"]["lastname"]


    @allure.title("Verify Update Multiple Fields Successfully")
    @allure.description(
        "Verify user can update multiple booking fields successfully."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "test_data",
        [
            UPDATE_DATA["tc12_update_multiple_fields"]
        ],
        ids=[
            "TC12-Update-Multiple-Fields"
        ]
    )
    def test_update_multiple_fields(
        self,
        booking_client,
        booking_id,
        headers,
        test_data
    ):

        with allure.step("Send Update Booking Request"):

            response = booking_client.update_booking(
                booking_id,
                test_data["payload"],
                headers
            )

        allure.attach(
            str(test_data["payload"]),
            name="Request",
            attachment_type=allure.attachment_type.JSON
        )

        allure.attach(
            str(response.json()),
            name="Response",
            attachment_type=allure.attachment_type.JSON
        )

        with allure.step("Verify Status Code"):

            assert response.status_code == \
                test_data["expected_status"]

        with allure.step("Verify Updated Response"):

            response_data = response.json()

            assert response_data["firstname"] == \
                test_data["payload"]["firstname"]

            assert response_data["lastname"] == \
                test_data["payload"]["lastname"]

            assert response_data["totalprice"] == \
                test_data["payload"]["totalprice"]

            assert response_data["depositpaid"] == \
                test_data["payload"]["depositpaid"]

        with allure.step("Verify Data Saved Successfully"):

            verify_data = booking_client.get_booking(
                booking_id
            ).json()

            assert verify_data["firstname"] == \
                test_data["payload"]["firstname"]

            assert verify_data["lastname"] == \
                test_data["payload"]["lastname"]

            assert verify_data["totalprice"] == \
                test_data["payload"]["totalprice"]

            assert verify_data["depositpaid"] == \
                test_data["payload"]["depositpaid"]


    @allure.title("Verify Update Booking With Fake Token")
    @allure.description(
        "Verify API rejects update request when using invalid token."
    )
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    @pytest.mark.parametrize(
        "test_data",
        [
            UPDATE_DATA["tc13_fake_token"]
        ],
        ids=[
            "TC13-Fake-Token"
        ]
    )
    def test_update_booking_with_fake_token(
        self,
        booking_client,
        booking_id,
        test_data
    ):

        fake_headers = {

            "Content-Type": "application/json",

            "Accept": "application/json",

            "Cookie": f"token={test_data['token']}"
        }

        payload = {
            "lastname": "Hack"
        }

        with allure.step("Send Update Request With Fake Token"):

            response = booking_client.update_booking(
                booking_id,
                payload,
                fake_headers
            )

        allure.attach(
            str(payload),
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