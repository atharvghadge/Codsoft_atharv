import random
import string

def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password using random.choices
    password = ''.join(random.choices(characters, k=length))

    return password

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired password length: "))

            if length <= 0:
                print("Please enter a valid positive length.")
                continue

            password = generate_password(length)
            print("Generated Password: " + password)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
