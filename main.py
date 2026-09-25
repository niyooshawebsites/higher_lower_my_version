from art import logo, vs
from game_data import data
import random

def print_score(s, g):
    if s > 0 and g:
        print(f'You are right. Your current score: {s}')
    else:
        print(f'You got it wrong. Your final score: {s}')
        
def random_data():
    index = random.randint(0, len(data) - 1)
    option = data[index]
    data.pop(index)
    return option

score = 0
game_on = True

print(logo)

option1 = random_data()

while game_on:
    option2 = random_data()

    print_score(score, game_on)
    print(f"Compare A: {option1["name"]}, {option1["description"]}, from {option1["country"]}")

    print(vs)

    print(f"Compare B: {option2["name"]}, {option2["description"]}, from {option2["country"]}")
        
    reply = input("Who has more followers? Type 'A' or 'B': ").lower().strip()
    
    correct_ans = "a" if option1['follower_count'] > option2['follower_count'] else "b"
    
    make_shit = ""

    if correct_ans == 'a':
        make_shit = option1
    elif correct_ans == 'b':
        make_shit = option2

    if reply == correct_ans:
        score += 1
        option1 = make_shit
    else:
        game_on = False
        print_score(score, game_on)