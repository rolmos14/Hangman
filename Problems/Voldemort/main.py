import random


# work with this variable
n = int(input())

random.seed(n)
word = "Voldemort"
print(random.choice(word))
