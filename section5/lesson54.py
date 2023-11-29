# for loops with ranges
## ranges define the start and the beginning of the loop (how many times it runs)
### runs 9 times, to run 10 times range(1,11) - weird gotcha
for number in range (1, 10):
  print(number)

## range() can define a step, or how many numbers each iteration should take
### this for loop runs four times, printing numbers 1, 4, 7, 10
for number in range (1, 11, 3):
  print(number)