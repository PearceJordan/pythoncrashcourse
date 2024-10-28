class Character:
    def __init__(self, name, health, strength):
        self.name = name 
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"({self.name}): My name is {self.name}! My health is {self.health}")

    def instigate(self, opponent_name):
        print(f"({self.name}): Your health is lower than mine, {opponent_name}. I will take your things. Filthy curr.")

    def response(self):
        print(f"({self.name}): Good heavens!")

    def attack(self, opponent):
        opponent.health = opponent.health - self.strength
        print(f"{self.name} is attacking {opponent.name}, {self.name} deals {opponent.name} {self.strength} damage! {opponent.name} 's health is now {opponent.health} !")
        

character = Character("Gremlin #1", 100, 20)

character_2 = Character("Gremlin #2", 75, 25)


# print(character.name, character.health)

# print(character_2.name, character_2.health)

# character.greet()
# character_2.greet()

# character.instigate(character_2.name)

# character_2.response()

character.attack(character_2)