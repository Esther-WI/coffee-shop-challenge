class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string and have at least 3 characters")
        self._name = name

    @property
    def name (self):
        return self._name 
    