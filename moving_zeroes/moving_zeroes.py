'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # loop through arr starting at index 1
    pointer = 0
    for x in range(leng(arr) - 1):

    # if int is greater than 0, insert on left side of array
        if x > 0:
            arr.insert(arr[pointer], x)
        # if int is not greater than 0 move to next index
        else:
            pointer += 1
    # return mutated arr after last index has been checked


    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")