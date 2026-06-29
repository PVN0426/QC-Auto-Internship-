import pytest
import allure

from utils.file_utils import read_json_file

ALL_DATA = read_json_file(
    "data/booking_data.json"
)

AUTH_DATA = ALL_DATA["auth"]


@allure.epic("Restful Booker API")
@allure.feature("Authentication")
@allure.story("Login API")
@pytest.mark.api
class TestAuth:

    @allure.title("Verify Login API")
    @allure.description(
        "Verify login API with valid and invalid credentials."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "payload",
        [
            AUTH_DATA["tc01_valid_login"],
            AUTH_DATA["tc02_invalid_login"]
        ],
        ids=[
            "TC01-Valid-Login",
            "TC02-Invalid-Login"
        ]
    )
    def test_login(self, payload, booking_client):

        with allure.step("Send Login Request"):
            response = booking_client.login(
                payload["username"],
                payload["password"]
            )

        allure.attach(
            str(payload),
            name="Request",
            attachment_type=allure.attachment_type.JSON
        )

        allure.attach(
            str(response.json()),
            name="Response",
            attachment_type=allure.attachment_type.JSON
        )

        with allure.step("Verify Status Code"):
            assert response.status_code == payload["expected_status"]

        with allure.step("Verify Response Body"):

            if "expected_key" in payload:
                assert payload["expected_key"] in response.json()

            if "expected_reason" in payload:
                assert response.json()["reason"] == payload["expected_reason"]