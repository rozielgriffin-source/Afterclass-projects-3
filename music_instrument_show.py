from abc import ABC, abstractmethod

class Instrument(ABC):

    def __init__(self, name, category):
        self.name = name
        self.category = category

    def display_info(self):
        print(f"Instrument Name: {self.name}")
        print(f"Category: {self.category}")

    @abstractmethod
    def play_sound(self):
        pass

class Guitar(Instrument):

    def __init__(self, name, category, strings):
        super().__init__(name, category)
        self.strings = strings

    def play_sound(self):
        print(f"{self.name} will sound like WAZOW! with {self.strings}")

class Drum(Instrument):

    def __init__(self, name, category, drum_type):
        super().__init__(name, category)
        self.drum_type = drum_type

    def play_sound(self):
        print(f"{self.name} is a {self.drum_type} and sounds like: Boom Boom!")

class Flute(Instrument):

    def __init__(self, name, category, material):
        super().__init__(name, category)
        self.material = material

    def play_sound(self):
        print(f"{self.name} is made of {self.material} and sounds like: Swishh!")

instrument_1 = Guitar("Electric Guitar", "String Instrument", 6)
instrument_2 = Drum("Bass Drum", "Percussion Instrument", "small drum")
instrument_3 = Flute("Nose", "Blow Instrument", "Wood")

print("===== Music Instrument Sound Show =====")

instrument_1.display_info()
instrument_1.play_sound()
print()

instrument_2.display_info()
instrument_2.play_sound()
print()

instrument_3.display_info()
instrument_3.play_sound()
print()