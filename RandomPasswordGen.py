import random

password = []
placeholder = 0
choices = []


print('How long would you like your password to be?')

passLength = input()

while len(password) < int(passLength):
    password = password + [placeHolder]
    placeHolder = placeHolder + 1
    
while len(choices) < 3:
    print('Hello, what would you like your password to consist of?')
    print('1.Uppercase' '\n' '2.Lowercase' '\n' '3.Symbols' '\n' '4.Nothing Else')

    choice = input()
    choices = choices + [choice]
    if 1 in choices:

upperCaseLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                   'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
upperCaseLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                   'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                    's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
symbols = [ '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '-', '=', '_', '+', '[', ']', '{', '}',
            '|', ';', ':', ',', '.', '<', '>', '?', '~']
def randomUpperCase:
    random.randint
