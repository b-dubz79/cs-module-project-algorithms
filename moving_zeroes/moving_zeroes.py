'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # loop through arr starting at index 1
    front_pointer = 0
    # print('f pointer', front_pointer, arr[front_pointer])
    end_pointer = len(arr) - 1
    # print('end pointer', end_pointer, arr[end_pointer])
    while front_pointer <= end_pointer:
        # if fp is 0 and ep is not zero
        if arr[front_pointer] == 0 and arr[end_pointer] != 0:
            arr[front_pointer], arr[end_pointer] = arr[end_pointer], arr[front_pointer]
            front_pointer += 1
            end_pointer -= 1
        
        elif arr[front_pointer] != 0:
            front_pointer += 1
        
        elif arr[end_pointer] == 0:
            end_pointer -= 1

    return arr

        # # if fp is not zero and ep is zero
        # elif arr[front_pointer] != 0 and arr[end_pointer] == 0:
        #     print('got to first elif', arr[front_pointer])
        #     front_pointer += 1
        #     end_pointer -= 1
        
        # # if neither is zero
        # elif arr[front_pointer] != 0 and arr[end_pointer] != 0:
        #     print('got to second elif')
        #     front_pointer += 1
        #     end_pointer -= 1
        
        # # if both are zero
        # elif arr[front_pointer] == 0 and arr[end_pointer] == 0:
        #     print('got to LAST elif')
        #     front_pointer += 1
        #     end_pointer -= 1

            

    ## optimized
# def moving_zeroes(arr):
    # initialize a left and right pointer
    # lef is 0
    # right is last index in arr
    
    # use a while loop (best with pointers, gives more control) while left is <= right
        #if left points at a zero and right points at non-zero
            # swap left and right items in original arr
            # increment left 
            # decrement right
        # else
            # if left is non-zero:
                #increment left
            # if right is zero:
                # decrement right

    # return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")