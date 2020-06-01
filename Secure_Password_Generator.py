# Creating Memorable password generator using your own suggested input..

Replacer = (('s','$'), ('a', '@'), ('h', '#'), ('and','&'))

def passwordGenerator(password):
    for a, b in Replacer:
        password = password.replace(a, b)
    return password

if __name__ == '__main__':
    password = input("Enter password of your choice : " )
    password = passwordGenerator(password)

    print(f"Your Customaize password is: ", password)
