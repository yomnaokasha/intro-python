from pet import Pet


class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()
        print(f"feeding {self.first_name} {self.treats}")
        print(f"feeding {self.first_name} {self.pet_food}")

    def bathe(self):
        self.pet.noise()


pet = Pet(name="rowy", type="dog", tricks="wave")
our_person = Ninja("Mr. Nibbles", "James", "pizza", "burger", pet)
our_person.feed()
