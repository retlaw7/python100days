import art
import data
import random
#start game and initialize starting variables
print(art.logo)
game_over = False
rng_A = random.randint(0, len(data.list)-1)
a_subject = data.list[rng_A]
score = 0

#start game
while game_over != True:
    #display option A
    print(f"Compare A {a_subject['name']}, a {a_subject['description']},  from {a_subject['country']}")
    print(art.vs)

    #generate new option for B
    rng_B = random.randint(0, len(data.list) - 1)
    b_subject = data.list[rng_B]

    #duplicate checker
    while a_subject['name'] == b_subject['name']:
        rng_B = random.randint(0, len(data.list) - 1)
        b_subject = data.list[rng_B]

    #display option for B
    print(f"Against B {b_subject['name']}, a {b_subject['description']},  from {b_subject['country']}")


    #ask for input
    choice = input("Who has more followers? A or B?").lower()
    if choice == "a" and a_subject['follower_count'] > b_subject['follower_count']:
        score += 1
        print(f"Correct! Your score = {score}")
        #set new a_subject
        a_subject = b_subject
    elif choice == "b" and a_subject['follower_count'] < b_subject['follower_count']:
        score += 1
        print(f"Correct! Your score = {score}")
        a_subject = b_subject
    elif choice == "a" and a_subject['follower_count'] < b_subject['follower_count']:
        print(f"You lose! Your final score = {score}")
        game_over = True
    elif choice == "b" and a_subject['follower_count'] > b_subject['follower_count']:
        print(f"You lose! Your final score = {score}")
        game_over = True