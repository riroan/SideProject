

class Repository:
    def find_by_id(self, id: int):
        ...

    def find_all(self):
        ...

    def save(self, data):
        ...

    def delete_by_id(self, id: int):
        ...
