flight_thresholds_type = set[list[str]]
flight_search_type = dict[dict[str, str]]
flight_matches_type = set[list[str]]

class DataModel:
  def __init__(self):
    self.flight_thresholds: flight_thresholds_type | None = None
    self.flight_search: flight_search_type | None = None
    self.flight_matches: flight_matches_type | None = None

  def get_flight_thresholds(self) -> flight_thresholds_type:
    return self.flight_thresholds

  def set_flight_thresholds(self, flight_thresholds: flight_thresholds_type) -> None:
    self.flight_thresholds = flight_thresholds

  def get_flight_search(self):
    return
