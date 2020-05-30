secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("You have " + str(guess_limit) + " chances to guess the secret word")
while guess != secret_word and not out_of_guesses: # while loop keeps going if guess does not equal secret_word AND they are not out of guesses
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1 # This is the same as "guess_count = guess_count + 1"
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses. YOU LOSE!")
else:
    print("You win!")
