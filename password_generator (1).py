import random
import string

try:
    length = int(input("Enter desired password length: "))

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))

    print("Generated Password:", password)

except ValueError:
    print("Please enter a valid number for password length.")
