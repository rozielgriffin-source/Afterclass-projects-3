class Pet:
    def __init__(self, name, health):
        self.name = name
        self.__health = health

    def show_info(self):
        print(f"Pet Name: {self.name}")
        print(f"Health: {self.__health}")

    def care_action(self):
        print(f"{self.name} needs general care.")

    def set_health(self, new_health):
        if new_health >= 0 and new_health <= 100:
            self.__health = new_health
            print(f"{self.name}'s health is now {self.__health}.")
        else:
            print("Health must be between 0 and 100.")

class Dog(Pet):
    def care_action(self):
        print(f"{self.name} needs to be walked and played with.")

class Ferret(Pet):
    def care_action(self):
        print(f"{self.name} needs grooming and quiet rest.")

class Lizard(Pet):
    def care_action(self):
        print(f"{self.name} needs fresh vegetables and a warm basking spot.")

dog = Dog("Boss", 85)
ferret = Ferret("Whiskers", 75)
lizard = Lizard("Spike", 70)

pets = [dog, ferret, lizard]

print("===== My Pet Care Dashboard =====")

for pet in pets:
    pet.show_info()
    pet.care_action()
    print()

print("===== Updated Pet Health =====")

dog.set_health(90)
ferret.set_health(80)
lizard.set_health(85)

print("===== Final Vet Pet Care =====")

for pet in pets:
    pet.show_info()
    print()