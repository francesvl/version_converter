def encode (password):
    string = ""
    value = 0
    for i in range (0, len(password)):
        value = int(password[i]) + 3
        string += str(value)
    return string


def main():
    encoded = None
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        menu_selection = int(input("Please enter an option: "))
        if menu_selection == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!")
        elif menu_selection == 2:
            decoded = decode(encoded)
            print("The encoded password is " + encoded + " and the original password is " + decoded + ".")
        elif menu_selection == 3:
            break

if __name__ == '__main__':
    main()
