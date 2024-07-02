import random

def game():
  hiddenNum = random.randint(0,100)

  while True:
    guessedNum = int(input("What is your next guess?: "))
    if guessedNum == hiddenNum:
      print("Congratulations you won!")
      play_again = input("If you want to play again type Y")
      if play_again == "Y":
        game()
      else:
        break;
    elif guessedNum > hiddenNum:
      print("Your guess is too high")
    else:
      print("Your guess is too low")

game()