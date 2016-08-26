def alphabet_position(letter):
    alphas = 'abcdefghijklmnopqrstuvwxyz'
    for i in letter:
        o = ord(i)  #ord value for letter determines if it is capital and lowercase letters
        if o > 96:
            position = alphas.index(i) # position gives the numerical location of letter in alphabet
        else:
            o < 91
            lwrcse = i.lower()
            position = alphas.index(lwrcse)

    return position
#print(alphabet_position("t"))
#print(alphabet_position("T"))




def rotate_character(char,rot):
    alphas2 = 'abcdefghijklmnopqrstuvwxyz'
    final_alpha = ""

    for j in char:
        newChar = ""

        if j.isalpha() == True:
            position_2 = alphabet_position(j) # alphabet_position function is used to identify position of char in the alphabet_position
            new_position = position_2 + rot  # rotate value is added to position of char to determine the location of new alphabet_position
            o = ord(j)    # ord value will be used to preserve the capitalization of char

        else:
            return char

        if new_position >= 26:
            wrapValue = new_position % 26 # if new_postion is above 26 the wrapValue will determine the location the new alphabet_position
            newChar = newChar + alphas2[wrapValue]  # Temporarily holds the new letter in case it should be capitalized

        else:
            newChar = newChar + alphas2[new_position]
        if o < 91:                          # determine if shifted character is capital
            newChar_upr = newChar.upper()
            final_alpha = final_alpha + newChar_upr

        else:
            final_alpha = final_alpha + newChar # if shifted character is not capital the lowercase is retruned

    return final_alpha
#print(rotate_character("a",9))
#print(rotate_character("c",27))
#print(rotate_character("Z",2))
