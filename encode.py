def encode(password):
    encoded_password = ""
    for char in password:
        encoded_char = (int(char) + 4) % 10
        encoded_password += str(encoded_char)
    return encoded_password

def main():
    while True:
        print("\nMenu:")
        print("1. Encode Password")
        print("2. Quit")

        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            password = input("Enter an 8-digit password (integers only): ")
            if len(password) == 8 and password.isdigit():
                encoded_password = encode(password)
                print("Encoded Password:", encoded_password)
            else:
                print("Invalid password. Please enter an 8-digit integer.")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()