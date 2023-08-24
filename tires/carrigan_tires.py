from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tires_array):
        self.tires_array = tires_array

    def needs_service(self):
        return any(worn_level >= 0.9 for worn_level in self.tires_array)