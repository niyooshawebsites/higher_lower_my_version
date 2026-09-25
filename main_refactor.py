from art import logo, vs
from game_data import data
import random

def get_random_account():
    """Return a random account and remove it from the available data"""
    return data.pop(random.randrange(len(data)))

def display_account(label, account):
    """Display an account"""
    print(
        f"Compare {label}: "
        f"{account['name']}, "
        f"{account['description']}, "
        f"from {account['country']}"
    )
    
def get_correct_answer(account_a, account_b):
    """Return a or b depending which account has more followers"""
    if account_a["follower_count"] > account_b["follower_count"]:
        return 'a'
    return 'b'

def play_game():
    score = 0 
    account_a = get_random_account()
    
    print(logo)
    
    while True:
        account_b = get_random_account()
        
        display_account("A", account_a)
        print(vs)
        display_account("B", account_b)
        
        answer = input("Who has more followers? Type 'A' or 'B': ").lower().strip()
        
        correct_ans = get_correct_answer(account_b, account_b)
        
        if answer != correct_ans:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
        
        score += 1
        account_a = account_b
        
        print(f"You're right! Current score: {score}")
        print()
        
play_game()