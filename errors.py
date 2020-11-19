
class Errors():
    error_names = []
    found_descriptions = []

    def __init__(self):
        self.error_names = []
        self.found_descriptions = []

    def insert_error(self, error_name, error_description):
        self.error_names.append(error_name)
        self.found_descriptions.append(error_description)

