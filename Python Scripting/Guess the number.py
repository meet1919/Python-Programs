#GuesstheNumber
print("Guess the number between 1 to 10")
number = 7

i=0
while i<=10:
    guess = int(input())
    if guess == number:
        print("You guessed the correct number")
        print("You guessed in the", i+1, "th try.")

    elif guess <= number:
        print("Your guess is too low. Try one more time")

    elif guess >= number:
        print("You guess is too high. Try one more time")

    else:
        print("You were't able to guess the number. FuckYou")

    i+=1


