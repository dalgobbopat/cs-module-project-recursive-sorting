# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    neg_inf = float('-inf')
    merged_arr = [neg_inf] * elements

    has_shifted = False
    while(len(arrA) > 0) and (len(arrB) > 0):
        if arrA[0] < arrB[0]:
            smallest_value = arrA.pop(0)
        elif arrB[0] < arrA[0]:
            smallest_value = arrB.pop(0)
            has_shifted = True
        insertion_point = merged_arr.index(neg_inf)
        merged_arr[insertion_point] = smallest_value

    if (len(arrA) > 0) and (len(arrB) == 0):
        for item in arrA:
            insertion_point = merged_arr.index(neg_inf)
            merged_arr[insertion_point] = item
    elif (len(arrB) > 0) and (len(arrA) == 0):
        for item in arrB:
            insertion_point = merged_arr.index(neg_inf)
            merged_arr[insertion_point] = item


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])


    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

