def guess_animal(guess,animal):
    global score
    guessing = True
    attempts = 0
    while guessing and attempts < 3:
        if guess.lower() == animal.lower():
            print("Correct Answer")
            score = score + 1
            guessing = False
        else:
            if attempts < 2:
                guess = input("Wrong Answer, Try Again ")

            attempts = attempts + 1
    if attempts == 3:
        print("The correct answer is", animal)

score = 0

print("Lets play guess the animal game")

guess1 = input("Which bear lives at the North Pole? ")
guess_animal(guess1, 'Polar Bear')

guess2 = input("Which is the fastest land animal? ")
guess_animal(guess2, "Cheetah")

guess3 = input("Which is the larget animal? ")
guess_animal(guess3, "Blue Whale")

print("Your Score is ", score)