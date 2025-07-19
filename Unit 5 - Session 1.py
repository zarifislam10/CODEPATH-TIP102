# Problem 1


class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and all(c.isalpha() or c.isspace() for c in new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase updated")
        else:
            print("Invalid catchphrase")

    def add_item(self, item_name):
        
        xxx = "acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"
        for i in xxx:
            if i in item_name:
                self.furniture.append(i)

            

# Problem1        
# Instantiate your villager here

apollo = Villager("Apollo", "Eagle", "pah")

# Problem 2

bones = Villager("Bones", "Dog", "yip yip")

print(bones.greet_player("Sam"))

print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 

# Problem 3
bones.catchphrase = "ruff it up"

print(bones.greet_player("Samia"))

# Problem 4

alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

# Problem 5

alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)

