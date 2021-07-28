import random

def guess(x):
  random_number = random.randint(1, x)
  guess = 0
  while (guess != random_number): 
    guess = int(input(f'Guess a number between 1 and {x}: '))
    if guess < random_number:
      print("Guess again, too low")
    elif guess > random_number:
      print("Guess again, too high")
  print(f"Congrats, you have guessed the number, which was {random_number} correctly")

guess(10)


def computer_guess(x):
  low = 1
  high = x
  feedback = ""

  while feedback != c