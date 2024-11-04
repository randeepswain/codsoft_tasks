import string
import random

def main():

    length = int(input("Enter the length of the password: "))
    difficulty = int(input("Enter the difficulty level (1 - Simple, 2 -Medium, 3 - Complex): "))

    print("Generated password:", generate_pass(length, difficulty))


def generate_pass(length, difficulty):

    if difficulty == 1:
        # Simple: Only Digits or Numbers
        chars = string.digits
    elif difficulty == 2:
        # Medium: Lowercase + Uppercase + Digits
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    elif difficulty == 3:  
        # Complex: Lowercase + Uppercase + Digits + Special characters
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    else:
        return "Invalid difficulty level.Please choose 1, 2 or 3"

    chosen_chars = []
    for _ in range(length):
        chosen_chars.append(random.choice(chars))
    password = ''.join(chosen_chars)
    return password

main()
