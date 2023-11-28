# can import libraries into python without a package manager - awesome (but dangerous and can get hard to debug)
import random

# defines a random number between 1 and 10
random_sideeger = random.randint(1, 10)
print(random_sideeger)

## random between 0.000 - 0.999....
random_float = random.random()
print(random_float)

## random between 0.0000 and 5 - multiplying random float by a whole number increases the range of randomness
## from 0 to below the whole number
random_float = random.random()
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")