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

def roll_dices(dices):
    return [dice.roll() for dice in dices]

def play_game(players):
    dices = [Dice() for _ in range(len(players))]
    scores = {player: sum(roll_dices(dices)) for player in players}
    
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
            scores[player] = max(roll_dices([Dice()]))
            print(f"{player} rolls again and gets {scores[player]}")
    
    winner = max(scores, key=scores.get)
    print(f"Winner is {winner} with score {scores[winner]}!")

# Example usage
players = ["Alice", "Bob", "Charlie"]
play_game(players)
