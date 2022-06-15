"""
Create a function that takes an object as an argument and returns a string with facts about the city. The city facts will need to be extracted from the object's three properties:
    name
    population
    continent

cityFacts({
  name: "Paris",
  population: "2,140,526",
  continent: "Europe"
}) ➞ "Paris has a population of 2,140,526 and is situated in Europe"

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

def city_facts(input):
    if verify_city(input):
        return input["name"] + " has a population of "+ input["population"] +" and is situated in "+ input["continent"]
    else:
        return "Invalid input"


def test(input):
    #print(isDigit(input))
    #print(sumofdigits(input))
    #print(ispalindrome(input))
    print(city_facts(input))


city = {
    "name": "Paris",
    "population": "2,543,453",
    "continent": "Europe"
}

city1 = {
    "name": "Waverly",
    "population": "2,453",
    "continent": "USA"
}

city2 = {
    "mynM": "Waverly",
    "population": "2,453",
    "continent": "USA"
}

test(city)
test(city1)
test(city2)