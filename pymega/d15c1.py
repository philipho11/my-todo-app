import random

low_input = int(input("Enter the lower bound: "))
high_input = int(input("Enter the upper bound: "))

randnum = random.randint(low_input, high_input)

print(randnum)