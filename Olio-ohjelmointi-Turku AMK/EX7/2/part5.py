import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        self.value = 1
    
    def roll(self):
        self.value = random.randint(1, self.sides)
        return self.value
    
    def __repr__(self):
        return str(self.value)

class Player:
    def __init__(self, player_id: int, name: str):
        self._player_id = player_id
        self._name = name
        self.dice = Dice()
        self._pet = None  # Pet is initially None
    
    @property
    def player_id(self):
        return self._player_id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    def roll_dice(self):
        return self.dice.roll()
    
    def set_pet(self, pet):  # Method to set pet for the player
        self._pet = pet
    
    @property
    def pet(self):
        return self._pet
    
    def __str__(self):
        pet_info = f" | Pet: {self._pet}" if self._pet else " | No pet"
        return f"Player {self._player_id}: {self._name}{pet_info}"

class Mammal:
    def __init__(self, mammal_id: int, species: str, name: str, size: str, weight: float):
        self._mammal_id = mammal_id
        self._species = species
        self._name = name
        self._size = size
        self._weight = weight
    
    @property
    def mammal_id(self):
        return self._mammal_id
    
    @property
    def species(self):
        return self._species
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @property
    def size(self):
        return self._size
    
    @property
    def weight(self):
        return self._weight
    
    def __str__(self):
        return f"{self._species} - {self._name}, Size: {self._size}, Weight: {self._weight} kg"

def create_players(num_players):
    return {i: Player(i, f"Player{i}") for i in range(1, num_players + 1)}

def play_game(players, num_dices):
    scores = {player.name: sum(player.roll_dice() for _ in range(num_dices)) for player in players.values()}
    
    print("Initial Rolls:")
    for player, score in scores.items():
        print(f"{player}: {score}")
    
    while len(set(scores.values())) < len(scores):
        max_score = max(scores.values())
        tied_players = [p for p, s in scores.items() if s == max_score]
        
        if len(tied_players) == 1:
            break
        
        print("Tie detected! Rolling again...")
        for player in tied_players:
            scores[player] = max(Player(0, player).roll_dice())
            print(f"{player} rolls again and gets {scores[player]}")
    
    winner = max(scores, key=scores.get)
    print(f"Winner is {winner} with score {scores[winner]}!")

# Example usage for Dice game
num_players = int(input("Enter the number of players: "))
num_dices = int(input("Enter the number of dices to use: "))
players = create_players(num_players)

# Create mammals for pets
mammal1 = Mammal(1, "Elephant", "Dumbo", "Large", 6000)
mammal2 = Mammal(2, "Lion", "Simba", "Medium", 200)
mammal3 = Mammal(3, "Dog", "Buddy", "Small", 10)

# Assign pets to players
players[1].set_pet(mammal1)
players[2].set_pet(mammal2)
players[3].set_pet(mammal3)

# Print out players with their pets
for player in players.values():
    print(player)  # This will print each player and their assigned pet

# Start the game
play_game(players, num_dices)
