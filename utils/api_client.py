import requests
from utils.logger import get_logger

class BookingClient:

    def __init__(self):

        self.base_url = "https://restful-booker.herokuapp.com"
        self.session = requests.Session()
        self.logger = get_logger()

    def login(self, username, password):

        payload = {
            "username": username,
            "password": password
        }

        self.logger.info(
            f"Login API - Username: {username}"
        )

        response = self.session.post(
            f"{self.base_url}/auth",
            json=payload,
            verify=False
        )

        self.logger.info(
            f"Login Status: {response.status_code}"
        )
        self.logger.info(
            f"Login Response: {response.text}"
        )
        return response
        
    def create_booking(self, payload):
        self.logger.info(
            f"Create Booking Payload: {payload}"
        )
        response = self.session.post(
            f"{self.base_url}/booking",
            json=payload,
            verify=False
        )
        self.logger.info(
            f"Create Booking Status: {response.status_code}"
        )
        if response.status_code == 200:
            booking_id = response.json()["bookingid"]

            self.logger.info(
                f"Booking created successfully - ID={booking_id}"
            )
        return response

    def get_booking(self, booking_id):

        self.logger.info(
            f"Get Booking - ID={booking_id}"
        )

        response = self.session.get(
            f"{self.base_url}/booking/{booking_id}",
            verify=False
        )

        self.logger.info(
            f"Get Booking Status={response.status_code}"
        )

        return response

    def update_booking(self,
                   booking_id,
                   payload,
                   headers):
        self.logger.info(
            f"Update Booking - ID={booking_id}"
        )

        self.logger.info(
            f"Payload={payload}"
        )
        response = self.session.patch(
            f"{self.base_url}/booking/{booking_id}",
            json=payload,
            headers=headers,
            verify=False
        )
        self.logger.info(
            f"Update Status={response.status_code}"
        )
        if response.status_code == 200:

            self.logger.info(
                "Update Booking Successfully"
            )

        else:

            self.logger.error(
                f"Update Failed: {response.text}"
            )
        return response
        
    def delete_booking(self,
                   booking_id,
                   headers):
        self.logger.info(
            f"Delete Booking - ID={booking_id}"
        )
        response = self.session.delete(
            f"{self.base_url}/booking/{booking_id}",
            headers=headers,
            verify=False
        )
        self.logger.info(
            f"Delete Status={response.status_code}"
        )
        if response.status_code == 201:

            self.logger.info(
                "Delete Booking Successfully"
            )
        else:
            self.logger.error(
                f"Delete Failed: {response.text}"
            )
        return response
    
