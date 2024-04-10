# Bryan Zheng
def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = input("Please enter an option: ")
        if choice == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
        elif choice == '2':
            password = input(f"The encoded password is {encoded_password}, and the original password is {}")
            decoded_password = decode(password)
        elif choice == '3':
            break


def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3))
        encoded_password += encoded_digit
    return encoded_password


if __name__ == "__main__":
    main()