import random
uppercaseLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                   'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
lowercaseLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                   'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                    's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
symbols = [ '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '-', '=', '_', '+', '[', ']', '{', '}',
            '|', ';', ':', ',', '.', '<', '>', '?', '~']
password = []
placeHolder = 0
choices = []
options = ['1.Uppercase', '2.Lowercase', '3.Symbols', '4.Nothing Else']

print('How long would you like your password to be?')

passLength = int(input())

while len(password) < int(passLength):
    password = password + [placeHolder]
    placeHolder = placeHolder + 1

while len(choices) < 3:
    print('Hello, what would you like your password to consist of?')
    print("\n".join(options))

    choice = int(input())
    choices = choices + [choice]
    try:
        if 1 in choices:
            print('WOO!')
            del options[0]
        elif 2 in choices:
            print('NOO!')
            del options[1]
        elif 3 in choices:
            print('IDK')
            del options[2]
        elif 4 in choices:
            break
    except IndexError:
        print('Please enter a value in the list!')
        continue
    break
print('All done!, your password is ' + str(password))

def randomUppercase
    randomNumber = random.randint(0,26)
    randomUppercase = uppercaseLetters[randomNumber]
    global randomUppercase

def randomLowercase
    randomNumber = random.randint(0,26)
    randomLowercase = lowercaseLetters[randomNumber]
    global randomLowercase
def randomSymbol
    randomNumber = random.randint(0,26)
    randomSymbol = Symbols[randomNumber]
    global randomSymbol
