# https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference
flight_search_criteria_type = list[
  dict[str: 'originLocationCode', str: 'destinationLocationCode', str: 'departureDate', str: 'adults', str: 'maxPrice']]
flight_search_type = set[list[str]]
flight_matches_type = list[dict[str:'price', str:'origin_airport', str:'destination_airport', str:'out_date']]
flight_thresholds_type = dict[str:'prices', [list[dict[str:'city', str:'iataCode', str:'id']]]]
users_type = dict[str: 'users', [list[dict[str: 'timestamp', str: 'firstName', str: 'lastName', str: 'Email']]]]
user_emails_type = list[str: 'email']


class DataModel:
  """
  The DataModel class is designed to manage various types of data related to flight searches,
  flight matches, flight thresholds, and user information. It uses type hints to specify the
  expected data structures for each attribute, ensuring that the data conforms to the expected format.
  """

  def __init__(self):
    """
    Initializes the DataModel with the following attributes set to None:
    - flight_thresholds: Expected to be of type flight_thresholds_type.
    - flight_search: Expected to be of type flight_search_type.
    - flight_matches: Expected to be of type flight_matches_type.
    - flight_search_criteria: Expected to be of type flight_search_criteria_type.
    - users: Expected to be of type users_type.
    """
    self.flight_thresholds: flight_thresholds_type | None = None
    self.flight_search: flight_search_type | None = None
    self.flight_matches: flight_matches_type | None = None
    self.flight_search_criteria: flight_search_criteria_type | None = None
    self.users: users_type | None = None
    self.user_emails: user_emails_type | None = None

  def get_flight_thresholds(self) -> flight_thresholds_type:
    """
    Returns the current value of flight_thresholds.
    """
    return self.flight_thresholds

  def set_flight_thresholds(self, flight_thresholds: flight_thresholds_type) -> None:
    """
    Sets a new value for flight_thresholds.

    Args:
        flight_thresholds (flight_thresholds_type): The new flight thresholds data.
    """
    self.flight_thresholds = flight_thresholds

  def get_flight_search_criteria(self):
    """
    Returns the current value of flight_search_criteria.
    """
    return self.flight_search_criteria

  def set_flight_search_criteria(self, flight_search_thresholds: flight_search_criteria_type) -> None:
    """
    Sets a new value for flight_search_criteria.

    Args:
        flight_search_thresholds (flight_search_criteria_type): The new flight search criteria data.
    """
    self.flight_search_criteria = flight_search_thresholds

  def get_flight_search(self) -> flight_search_type:
    """
    Returns the current value of flight_search.
    """
    return self.flight_search

  def set_flight_search(self, flight_search: flight_search_type) -> None:
    """
    Sets a new value for flight_search.

    Args:
        flight_search (flight_search_type): The new flight search data.
    """
    self.flight_search = flight_search

  def update_flight_search(self, flight_search_result) -> None:
    """
    Updates the flight_search attribute with new search results.

    Args:
        flight_search_result: The new flight search results to update.

    Note:
        There is a potential issue in this method as it attempts to call update on a set,
        which is not a valid operation for sets in Python.
    """
    self.flight_search = self.flight_search.update(flight_search_result)

  def get_flight_matches(self) -> flight_matches_type:
    """
    Returns the current value of flight_matches.
    """
    return self.flight_matches

  def set_flight_matches(self, flight_match: flight_matches_type) -> None:
    """
    Sets a new value for flight_matches and prints the current flight matches.

    Args:
        flight_match (flight_matches_type): The new flight matches data.
    """
    self.flight_matches = flight_match
    print(self.get_flight_matches())

  def get_users(self) -> users_type:
    """
    Returns the current value of users.
    """
    return self.users

  def set_users(self, users: users_type) -> None:
    """
    Sets a new value for users.

    Args:
        users (users_type): The new users data.
    """
    self.users = users

  def get_user_emails(self) -> user_emails_type:
    return self.user_emails

  def set_user_emails(self, user_emails: user_emails_type) -> None:
    self.user_emails = user_emails
