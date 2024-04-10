# Bryan Zheng

def main():
    encoded_password = ""

    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = input("Please enter an option: ")

        if choice == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")

        elif choice == '2':
            if encoded_password:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
            else:
                print("No password has been encoded yet. Please encode a password first.\n")

        elif choice == '3':
            break

        else:
            print("Invalid option. Please try again.\n")


def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def decode(password):
    decoded_password = ""
    for digit in password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password


if __name__ == "__main__":
    main()
