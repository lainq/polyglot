class Position(object):
    def __init__(self, initial_position):
        assert isinstance(initial_position, int), "Expected an integer"
        self.position = initial_position

    def increment(self, increment_by=1):
        self.position += 1
        return self.position

    def decrement(self, decrement_by=1):
        self.position -= 1
        return self.position

    def current_character(self, data, increment_value=False):
        assert isinstance(data, list), "Data expected to be a string"
        if len(data) == self.position:
            return None

        return_value = data[self.position]
        if increment_value:
            self.increment()

        return return_value
