class Person:
    def __init__(self, name, member_id, loans=None):
        self._name = name
        self._member_id = member_id

    @property
    def name(self):
        return self._name

    @property
    def member_id(self):
        return self._member_id

    def __repr__(self):
        return f"{self.name} (ID: {self.member_id})"