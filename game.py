#another python
 from random import randint

x = int(input("Enter any number from 1 to 10: "))
y = randint(1, 10)

while y != x:
    print("Incorrect guess. Try again.")
    x = int(input("Enter any number from 1 to 10: "))

print("Congratulations! You have guessed the number correctly.")
