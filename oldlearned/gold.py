import random
the_number=random.randint(1,100)
guess = int(input("guess a number between 1 and 100:"))
tries = 0
while guess != the_number:
    if guess > the_number:
        print(guess,"was too high,try again.")
    if guess < the_number:
        print(guess,"was too low,try again.")
    guess = int(input("guess again:"))
    tries = tries + 1
print("you guess tries is",tries,guess,"it was the nmber!You win!")