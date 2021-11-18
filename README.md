# Flamby-api-test
**Project**: Flamby

**Endpoint(s)**: Get Reservation with specific date (http://flamxby.herokuapp.com/reservation/{year}/{month}/{day})

## Flamby API Get Reservation with specific date's Test Cases:
| ID | Name | Description | Result |
| :---| :---  | :--- | :--: |
| 1   | test_get_reservation_from_dates_successfully()  | Test the status code of getting the reservation from the date successfully   | Pass |
| 2   | test_reservation_id_get_reservation_from_dates_successfully()  | Test the reservation_id of getting the reservation from the date successfully.   | Pass |
| 3   | test_register_timestamp_get_reservation_from_dates_successfully()  | Test the register_timestamp of getting the reservation from the date successfully   | Pass |
| 4   | test_vaccinated_get_reservation_from_dates_successfully()  | Test the vaccinated of getting the reservation from the date successfully   | Pass |
| 5   | test_owner_get_reservation_from_dates_successfully()  | Test the owner of getting the reservation from the date successfully   | Pass |
| 6   | test_get_reservation_from_dates_wrong_parameters_type()  | Test the status code of getting the reservation from the date with the wrong parameters type   | Pass |
| 7   | test_get_reservation_from_dates_not_exist()  | Test the status code of getting the reservation from the date that does not exist   | Pass |
| 8   | test_get_reservation_from_negative_dates()  | Test the status code of getting the reservation from the date that are negative   | Pass |
| 9   | test_get_reservation_from_dates_content_type()  | Test the header content-type of getting the reservation from the date successfully  | Pass |
| 10   | test_get_reservation_from_dates_header_server()  | Test the header server of getting the reservation from the date successfully | Pass |