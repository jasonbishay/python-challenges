"""
Create a function that performs a Cesar shift with two inputs:
1: String to manipulate
2: number of chars to shift
Chars to protect A-Z
Passthrough unprotected Chars
"""

"""
Get ASCII values, 65-90 is A-Z
"""

def shift_char(char_to_shift, shift):
    char = ord(char_to_shift)
    if(char > 90 or char < 65):
        return chr(char)
    char += shift
    if char > 90:
        char = (char-90)+64
    
    return chr(char)
    

def unshift_char(char_to_shift, shift):
    char = ord(char_to_shift)
    if(char > 90 or char < 65):
        return chr(char)
    char -= shift
    if char < 65:
        char = (char+90)-64
    
    return chr(char)

def cesar_shift(input, shift):
    shifted_input = []
    for i in input:
        shifted_input.append(shift_char(i, shift))

    str = ""
    return str.join(shifted_input)

def cesar_unshift(input, shift):
    shifted_input = []
    for i in input:
        shifted_input.append(unshift_char(i, shift))

    str = ""
    return str.join(shifted_input)

#def cesar_unshift(input, shift):



def test(input, shift):
    shifted = cesar_shift(input, shift)
    unshifted = cesar_unshift(shifted, shift)
    print("\"Encrypted\" Text: "+shifted)
    print("\"Decrypted\" Text: "+ cesar_unshift(shifted, shift))
    assert input == unshifted, "Shift/Unshift didn't match"


test("HELLO BOBBYZX",3)
test("432",3)
