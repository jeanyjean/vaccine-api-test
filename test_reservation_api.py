"""Unit tests for the Reservation API"""
import unittest
import requests


class ReservationApiTest(unittest.TestCase):
    """
    Class for testing the get reservation from specific date from the Reservation API of Flamby(Government) module.
    """

    def setUp(self):
        """
        Setup function for setting the variable response as the API endpoint.
        """
        self.response = requests.get("http://flamxby.herokuapp.com/reservation/2021/10/20")

    def test_get_reservation_from_dates_successfully(self):
        """
        Test the status code of getting the reservation from the date successfully.
        """
        self.assertEqual(self.response.status_code, 200)
    
    def test_reservation_id_get_reservation_from_dates_successfully(self):
        """
        Test the reservation_id of getting the reservation from the date successfully.
        """
        self.response_content = self.response.json()

        self.assertEqual(self.response_content[0]["reservation_id"], 8)
    
    def test_register_timestamp_get_reservation_from_dates_successfully(self):
        """
        Test the register_timestamp of getting the reservation from the date successfully.
        """
        self.response_content = self.response.json()

        self.assertEqual(self.response_content[0]["register_timestamp"], "2021-10-20T17:12:39.738000")
    
    def test_vaccinated_get_reservation_from_dates_successfully(self):
        """
        Test the vaccinated of getting the reservation from the date successfully.
        """
        self.response_content = self.response.json()

        self.assertEqual(self.response_content[0]["vaccinated"], False)
    
    def test_owner_get_reservation_from_dates_successfully(self):
        """
        Test the owner of getting the reservation from the date successfully.
        """
        self.response_content = self.response.json()
        self.owner = {
                        "name": "foo",
                        "surname": "rock",
                        "birth_date": "2001-11-18",
                        "citizen_id": "1234567848204",
                        "occupation": "programmer",
                        "address": "bangkok"
                    }

        self.assertEqual(self.response_content[0]["owner"], self.owner)

    def test_get_reservation_from_dates_wrong_parameters_type(self):
        """
        Test the status code of getting the reservation from the date with the wrong parameters type.
        """
        self.response = requests.get("http://flamxby.herokuapp.com/reservation/c/d/a")
        self.assertEqual(self.response.status_code, 422)

    def test_get_reservation_from_dates_not_exist(self):
        """
        Test the status code of getting the reservation from the date that does not exist.
        """
        self.response = requests.get("http://flamxby.herokuapp.com/reservation/2050/10/20")
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.json(), [])
    
    def test_get_reservation_from_negative_dates(self):
        """
        Test the status code of getting the reservation from the date that are negative.
        """
        self.response = requests.get("http://flamxby.herokuapp.com/reservation/-2050/-10/-20")
        self.assertEqual(self.response.status_code, 500)

    def test_get_reservation_from_dates_content_type(self):
        """
        Test the header content-type of getting the reservation from the date successfully.
        """
        self.assertEqual(self.response.headers["Content-Type"], "application/json")
    
    def test_get_reservation_from_dates_header_server(self):
        """
        Test the header server of getting the reservation from the date successfully.
        """
        self.assertEqual(self.response.headers["Server"], "uvicorn")
    
if __name__ == '__main__':
    unittest.main()