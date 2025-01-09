from utility import *
mode = ask('Alternating or vowels?')
vowels = ['a','e','i','o','u','y']

def altCaps(str):
    count = 0
    temp = ''
    for letter in str:
        if count %2 == 1:
            temp += letter.upper()
        else:
            temp += letter.lower()
        count+=1
    return temp
def vowelCaps(str):
    temp = ''
    for letter in str:
        if searchList(letter.lower(),vowels):
            temp += letter.upper()
        else:
            temp += letter.lower()
    return temp
being_bothersome = True
while being_bothersome:
    string = ask("Say Something!")
    if string == '':
        being_bothersome = False
        print("Ok fine, I'll stop now.")
        break
    if mode == 'vowels':
        print(vowelCaps(string))
    else:
        print(altCaps(string))
