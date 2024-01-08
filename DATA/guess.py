#guessing game
secretWord = "bingo"
guess = " "
guess_count = 0
guess_limit = 3
out_of = False

while guess != secretWord and not(out_of):
    if guess_count < guess_limit:
        guess = raw_input("Enter guess : ")
        guess_count += 1
    else:
        out_of = True
if out_of:
    print("Out of Guesses \n you lose!!!")
else:
    print ("you win!")
