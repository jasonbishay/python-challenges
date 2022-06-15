"""
Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects like { "name": "John", "top_note": 5 }.
"""
"""

def verify_city(input):
    if not "name" in input:
        return False
    elif not "population" in input:
        return False
    elif not "continent" in input:
        return False
    else:
        return True
"""

def get_top_note(input):
    return max(input)

def get_new_obj(input):
    newInput = {
        "name": input["name"],
        "top_note": get_top_note(input["notes"])
    }
    return newInput

def top_notes(input):
    newList=[]
    for i in input:
        newList.append(get_new_obj(i))

    return newList



def test(input):
    print(top_notes(input))

# { "name": "John", "notes": [3, 5, 4] }
obj1 =[ {"name": "John", "notes": [3,4,5]}, 
       {"name": "Bob", "notes": [7,2,1]}
]


test(obj1)
#test(city1)
#test(city2)