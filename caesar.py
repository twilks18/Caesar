from helpers import alphabet_position, rotate_character

from sys import argv

def user_input_is_valid(argv):

    if len(argv) < 2:
        return False

    x = argv[1]
    if x.isdigit() == False:
        return False
    return True

def encrypt(text,rot):
    encrypted =""  # empty sting will hold encrypted message
    for k in text:
        encrypts = rotate_character(k,rot) # temporarily stores the new encrypted characters within the text
        encrypted = encrypted + encrypts

    return encrypted


#text = input("Type the message that you would like to encrypt.")
#rot= int(input("How far would you like to shift the letters?"))
#print(user_input_is_valid(argv))
#if user_input_is_valid(argv):
    #print(encrypt(text, int(argv[1])))
#else:
    #print("usage: python3 caesar.py n" )
#print(encrypt("HOPE THIS WORKS!", 2))
#print(encrypt("Ta'Neisha L. Wilks" , 14))
