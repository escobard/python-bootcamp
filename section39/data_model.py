class DataModel:
  def __init__(self):
    self.flight_thresholds: set[list[str]] | None
    self.flight_search: dict[dict[str, str]] | None
    self.flight_matches: set[list[str]] | None
