"""
This function accepts an encoded string as a parameter. This string will contain a first name, last name, and an id.

Values in the string can be separated by any number of zeros. The id is a numeric value but will contain no zeros. The function should parse the string and return a Python dictionary that contains the first name, last name, and id values.

An example input would be "Robert000Smith000123". The function should return the following using that input:

{ "first_name": "Robert", "last_name": "Smith", "id": "123" }
"""

def get_dict(input):
    split = input.split("0")
    while "" in split:
        split.remove("")
    
    return {
        "first_name": split[0],
        "last_name":  split[1],
        "id_name": split[2]
    }




def test(input):
    #print(isDigit(input))
    #print(sumofdigits(input))
    #print(ispalindrome(input))
    print(get_dict(input))


test("Robert000Smith000123")

test("Robert0Smith0000000000000012300000000000000")