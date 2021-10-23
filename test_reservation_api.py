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
        Test the header of getting the reservation from the date successfully.
        """
        self.assertEqual(self.response.headers["Content-Type"], "application/json")
    
if __name__ == '__main__':
    unittest.main()