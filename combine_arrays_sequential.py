"""
Create a function that accepts two arrays and determines after combined if they are sequential.

"""
# this method takes in 2 arrays, combines them and sorts them
def combine_sort(array1, array2):
    combined_array = array1 + array2
    for i in combined_array:
        if not isinstance(i,int):
            raise ValueError("Input is not all integers")
    return sorted(combined_array)


def verify_sequential(input_array):
    # loop through array, check if next value is +1 to current value
    for i in input_array:
        if i+1 == len(input_array):
            break
        if input_array[i+1] != input_array[i+1]:
            return False
    # check last element
    if input_array[len(input_array)-1] != input_array[len(input_array)-2]+1:
        return False

    return True

def isTwoArraysSequential(array1, array2):
    try:
        combined = combine_sort(array1, array2)
    except:
        return False
    #print(combined)
    return verify_sequential(combined)

def test(array1, array2):
    print(isTwoArraysSequential(array1, array2))

   
   
# Happy Case
test([1,5,8,3],[2,4,7,6])

# another happy case, one array empty
test([0,1,2,3,4,5],[])

# invalid input
test(["a",1,2],[5,7,9])

# should be false, duplicates
test([1,5,8,3],[2,4,7,6,8])

# should be false
test([1,5,0,3],[2,4,7,6,8])

# should be false, last element
test([1,5,10,3],[2,4,7,6])

# should be false, last element
test([1,5,10,3],[2,4,7,6])
