import random
import sys
level=1
while True:
    try:
      level=int(input("Level: "))
    except ValueError:
        continue
    if level>0:
        break
number=random.randint(1,level)
while True:
    try:
        guess=int(input("Guess: "))

    except ValueError:
        continue
    if guess<=0:
        continue
    if guess==number:
        sys.exit("Just right!")
    elif guess>number:
        print("Too large!")
    else:
        print("Too small!")
