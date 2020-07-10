
def binary_search_recursive(arr, x, low, high):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_recursive(arr, x, low, mid-1)
        else:
            return binary_search_recursive(arr, x, mid+1, high)
    return -1


def binary_search(arr, x):
    high = len(arr) - 1
    low = 0
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if x < arr[mid]:
            high = mid - 1
        elif x > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1




if __name__ == '__main__':
    arr = [1, 4, 2, 5, 3, 7, 6]
    print(binary_search(arr, 4))
    print(binary_search_recursive(arr, 4, 0, len(arr)-1))
