flight_thresholds_type = dict[str, [list[dict[str:'city', str:'iataCode', str:'id']]]]
flight_search_type = set[list[str]]
flight_matches_type = set[list[str]]


class DataModel:
  def __init__(self):
    self.flight_thresholds: flight_thresholds_type | None = None
    self.flight_search: flight_search_type | None = None
    self.flight_matches: flight_matches_type | None = None

    # https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference
    self.flight_search_criteria = {
      "currencyCode": "CAD",
      "originDestinations": [
        # populate this with data from flight threshold
        # {
        #   "id": "1",
        #   "originLocationCode": "NYC",
        #   "destinationLocationCode": "MAD",
        #   "departureDateTimeRange": {
        #     "date": "2023-11-01",
        #     "time": "10:00:00"
        #   }
        # }
      ],
      "travelers": [
        {
          "id": "1",
          "travelerType": "ADULT"
        }
      ],
      "sources": [
        "GDS"
      ],
      "searchCriteria": {
        "maxFlightOffers": 2,
        "flightFilters": {
          "cabinRestrictions": [
            {
              "cabin": "BUSINESS",
              "coverage": "MOST_SEGMENTS",
              "originDestinationIds": [
                # populate this with total number of destination Ids from flight threshold
                # "1"
              ]
            }
          ]
        }
      }
    }

  def get_flight_thresholds(self) -> flight_thresholds_type:
    return self.flight_thresholds

  def set_flight_thresholds(self, flight_thresholds: flight_thresholds_type) -> None:
    self.flight_thresholds = flight_thresholds

  def get_flight_search(self) -> flight_search_type:
    return self.flight_search

  def set_flight_search(self, flight_search: flight_search_type) -> None:
    self.flight_search = flight_search

  # update parameter type to match flight data
  def update_flight_search(self, flight_search_result) -> None:
    self.flight_search = self.flight_search.update(flight_search_result)

  def get_flight_matches(self) -> flight_matches_type:
    return self.flight_matches

  def set_flight_matches(self, flight_match: flight_matches_type) -> None:
    self.flight_matches = flight_match

  # update parameter type to match flight data
  def update_flight_matches(self, flight_match_result) -> None:
    self.flight_matches = self.flight_matches.update(flight_match_result)
