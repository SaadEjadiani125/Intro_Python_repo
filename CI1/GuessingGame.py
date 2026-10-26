import random
 
secret = random.randint(1, 100)
guess = int(input("Your guess: "))

attempts = 0
while attempts<7:
    if guess < secret:
        print("Too low!")
    elif guess==secret:
        print(f"it took you: {attempts} attempts, Bravo!")
        break
    else:
        print("Too high!")
    guess = int(input("Your guess: "))
    attempts +=1
 
if guess!=secret:
    print("Lost? It was", secret)