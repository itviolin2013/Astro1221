class Observation:
    """A class representing an astronomical observation."""

    def __init__(self, target_name, filter_name):
        self.target_name = target_name
        self.filter_name = filter_name

    def start_obs(self):
        """Print a message indicating the observation is starting."""
        print(f"Starting observation of {self.target_name} in {self.filter_name}")
