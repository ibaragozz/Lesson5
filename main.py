class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def eat(self):
        print(f” {self.name} сел кушать”)
        self.power += 1

    def sleep(self):
        print(f” {self.name} лег поспать”)
        self.endurance += 2

    def fight(self):
        print(f” {self.name} сражается”)
        self.endurance -= 6

    def walk(self):
        print(f”имя воина - {self.name}”)
        print(f”цвет волос воина - {self.hair_color}”)
        print(f”сила воина - {self.power}”)
        print(f”выносливость воина - {self.endurance}”)