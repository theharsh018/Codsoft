import random
import string

def generate_password(length):
    # Define possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure password is at least 4 characters long for reasonable complexity
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None
    
    # Generate a password using random choices
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== PASSWORD GENERATOR ===")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        if password:
            print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
