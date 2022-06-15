"""
Create a function that takes two strings, code and guess as arguments, and returns the score in a dictionary.

The code and guess are strings of numeric digits
The color of the pegs are represented by numeric digits
no "peg" may be double-scored

"""


# method that returns the white result
def get_white(code, guess):
    white = 0
    unique_guess = set(guess)
    unique_guess = list(unique_guess)
    #print(unique_guess)
    for i in range(len(unique_guess)):
        if unique_guess[i] in code:
            white = white + 1
    return white


# method that returns the black result
def get_black(code, guess):
    black = 0
    for i in range(len(code)):
        if code[i] == guess[i]:
            black = black + 1
    return black

def guess_score(code, guess):
    code_array = list(code)
    guess_array = list(guess)
    hit = []
    black = 0
    white = 0
    for i in range(len(guess_array)):
        if code_array[i] == guess_array[i]:
            black = black + 1
        elif code_array[i] in guess_array:
            white = white+1

    retVal = {
        "black" : black,
        "white" : white
    } 
    print(retVal)
    return retVal

assert guess_score("1423", "5678"), {"black": 0, "white": 0}
assert guess_score("1423", "2222"), {"black": 1, "white": 0}
assert guess_score("1423", "1234"), {"black": 1, "white": 3}
assert guess_score("1423", "2211"), {"black": 0, "white": 2}
assert guess_score("2928", "7722"), {"black": 1, "white": 1}
assert guess_score("4845", "6446"), {"black": 1, "white": 1}