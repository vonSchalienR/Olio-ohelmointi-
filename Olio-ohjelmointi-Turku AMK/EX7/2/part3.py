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
    
    def __str__(self):
        return f"Player {self._player_id}: {self._name}"

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

# Example usage
num_players = int(input("Enter the number of players: "))
num_dices = int(input("Enter the number of dices to use: "))
players = create_players(num_players)
play_game(players, num_dices)
