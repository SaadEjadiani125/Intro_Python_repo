import random
from statistics import mean

def roll(n):
    results = []
    for _ in range(n):
        results.append(random.randint(1,6))
    return results
random.seed(3)
