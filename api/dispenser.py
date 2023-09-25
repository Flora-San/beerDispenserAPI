# dispenser.py

class Dispenser:
    def __init__(self, dispenser_id, name):
        self.dispenser_id = dispenser_id
        self.name = name
        self.status = "off"

    def to_dict(self):
        return {
            "id": self.dispenser_id,
            "name": self.name,
            "status": self.status,
        }

    def update_status(self, status):
        self.status = status
