class Custom_exception(Exception):
    def __init__(self, error_id = 1, message = "Artist not found."):
        self.error_id = error_id
        self.message = message