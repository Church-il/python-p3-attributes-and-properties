approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

class Dog:
    def __init__(self, name="Unknown", breed="Unknown"):
        self._name = "Unknown"
        self._breed = "Unknown"
        self._name_valid = self.set_name(name)
        if self._name_valid:
            self.set_breed(breed)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
            return True
        else:
            print("Name must be string between 1 and 25 characters.")
            return False

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in approved_breeds:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)