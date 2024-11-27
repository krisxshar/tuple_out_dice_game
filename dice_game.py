import random

def roll_dice():
    """Roll three dice and return their values as a tuple."""
    return tuple(random.randint(1, 6) for _ in range(3))

def display_scores(scores):
    """Display the current scores of all players."""
    print("\nCurrent Scores:")
    for player, score in scores.items():
        print(f"{player}: {score} points")
    print()
    
def tuple_out(dice):
    """Check if all three dice have the same value."""
    return len(set(dice)) == 1

def fixed_dice(dice):
    """Identify dice that are fixed (appear twice)."""
    counts = {num: dice.count(num) for num in set(dice)}
    return [num for num, count in counts.items() if count == 2]

def play_turn(player):
    """Handle a single player's turn."""
    print(f"\n{player}'s turn!")
    dice = roll_dice()
    print(f"Initial roll: {dice}")

    while True:
        if tuple_out(dice):
            print("Tuple out! You score 0 points this turn.")
            return 0
        
        fixed = fixed_dice(dice)
        if fixed:
            print(f"Fixed dice: {fixed} (cannot re-roll these)")

        else:
            print("No fixed dice.")

        re_roll_indices = []
        for i, die in enumerate(dice):
            if die not in fixed:
                re_roll = input(f"Re-roll die {i+1} (value {die})? (y/n): ").strip().lower()
                if re_roll == 'y':
                    re_roll_indices.append(i)
                    
        if not re_roll_indices:
            break # Player chooses to stop their turn
        
        # Re-roll the selected dice
        for i in re_roll_indices:
            dice = tuple(random.randint(1, 6) if idx == i else die for idx, die in enumerate(dice))
        print(f"New roll: {dice}")
        
    score = sum(dice)
    print(f"End of turn! You score {score} points.")
    return score

def tuple_out_game():
    """Run the Tuple Out Dice Game."""
    print("Welcome to the Tuple Out Dice Game!")
    target_score = 50
    players = input("Enter player names (comma-separated): ").strip().split(',')

    scores = {player.strip(): 0 for player in players}
    while all(score < target_score for score in score.values()):
        for player in players:
            scores[player.strip()] += play_turn(player.strip())
            display_scores(scores)

            if scores[player.strip()] >= target_score:
                print(f"{player.strip()} wins with {scores[player.strip()]} points!")
                return
            
if __name__ == "__main__":
    tuple_out_game()
