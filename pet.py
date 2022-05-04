class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5

    def noise(self):
        print("woooohoowwww")


our_pet = Pet("rowy", "dog", "wave")


our_pet.eat()
print(our_pet.energy)
print(our_pet.health)
