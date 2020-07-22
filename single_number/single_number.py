'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # sort array
    sort_arr(arr)
    # create pointer at index 0 then compare index 0 to index 1
    pointer = 0
    # loop through arr
    for x in range(pointer, len(arr) - 1):
        # if index[0] equals index[1], at 2 to pointer and repeat
        if arr[pointer] == arr[pointer + 1]:
            pointer += 2
        # if indexes don't match return first index in the comparison
        else:
            return x
    

def sort_arr(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

    