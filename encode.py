# Adnan Sanaulla
# Jake Marotta
def encode(password):
    encoded_password = ""
    for char in password:
        encoded_char = (int(char) + 3) % 10
        encoded_password += str(encoded_char)
    return encoded_password

def decode(encoded_password):
    decoded_password = ""
    for char in encoded_password:
        decoded_char = (int(char) - 3) % 10
        decoded_password += str(decoded_char)
    return decoded_password


def main():
    while True:
        print("\nMenu:")
        print("1. Encode Password")
        print("2. Decode Password")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            password = input("Enter an 8-digit password (integers only): ")
            if len(password) == 8 and password.isdigit():
                encoded_password = encode(password)
                print("Encoded Password:", encoded_password)
            else:
                print("Invalid password. Please enter an 8-digit integer.")
        elif choice == "2":
            encoded_password = input("Enter an 8-digit encoded password (integers only): ")
            if len(encoded_password) == 8 and encoded_password.isdigit():
                decoded_password = decode(encoded_password)
                print("Decoded Password:", decoded_password)
            else:
                print("Invalid password. Please enter an 8-digit integer.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()
