import random

class Character:
    def __init__(self, name, health, strength, damage):
        self.name = name 
        self.health = health
        self.strength = strength
        self.is_alive = True

    def greet(self):
        print(f"({self.name}): My name is {self.name}! My health is {self.health}")

    def instigate(self, opponent_name):
        print(f"({self.name}): Your health is lower than mine, {opponent_name}. I will take your things. Filthy curr.")

    def response(self):
        print(f"({self.name}): Good heavens!")

    def attack(self, opponent):
        damage = self.damage()
        print(f"{self.name} attacks {opponent.name}.")
        print(f"{self.name} does {damage} damage.")
        opponent.health = opponent.health - damage
        if (opponent.health < 0):
            opponent.is_alive = False
            print(f"{opponent.name} has died!")
        else: 
            print(f"{opponent.name} has {opponent.health} health remaining")
    
    def damage(self):
        return int(self.strength + random.randint(0, int(self.strength/2)) - self.strength/4)
        
        
character_1 = Character("Gremlin #1", 100, 20, 20)

character_2 = Character("Gremlin #2", 100, 20, 20)

while character_1.health > 0 and character_2.health > 0:
    if (random.randrange(0,2)) == 0:
         character_1.attack(character_2)
         if character_2.is_alive:
              character_2.attack(character_1)
    else:
         character_2.attack(character_1)
         if character_1.is_alive:
              character_1.attack(character_2)
    
    
   

# print(character_1.name, character_1.health, character_1.strength, character_1.damage)

# def attack(self, opponent):
#    return self.strength + random.randint(0, self.strength) - self.strength/4
    
# print(character_2.name, character_2.health)

# character_1.greet()
# character_2.greet()

# character_1.instigate(character_2.name)

# character_2.response()

# character_1.attack(character_2)