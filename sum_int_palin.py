"""
Checks if sum of digits in an int is a palindrome or not
"""

def isdigit(input):
    if input is None:
        return False
    try:
        int(input)
    except:
        return False
    
    return True

def sumofdigits(input):
    nums = [int for int in input]
    sum = 0
    for i in nums:
        sum = sum + int(i)
    
    return sum

def ispalindrome(input):
    nums = [int for int in input]
    j = len(nums)
    for i in nums:
        if int(i) != int(nums[j-1]):
            j = j-1
            return False 
        return True

def is_sum_palindrome(input):
    if not isdigit(input):
        print("Error: Input is not numeric")
        return 0

    sum = sumofdigits(input)
    print("Sum of the digits from input: "+input+" is: " + str(sum))
    if ispalindrome(str(sum)):
        return 1
    else:
        return 0


def test(input):
    #print(isDigit(input))
    #print(sumofdigits(input))
    #print(ispalindrome(input))
    print(is_sum_palindrome(input))



test("")
test("1")
test("56")
test("56542365")