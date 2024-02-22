class Student:
    def __init__(self, p_name):
        self._name = ''
        self.name = p_name

    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, p_name):
        if len(p_name) >= 3 and p_name.isalpha():
            self._name = p_name
        else:
            raise 'ValueError'
