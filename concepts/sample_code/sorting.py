import timeit

# Runtime: 0(n2) average and worst case. Memory: 0(1).
def bubble_sort(arr):
    n = len(arr)
    # traverse all array elements
    for i in range(n-1):
        # last i element will already be in place
        for j in range(0, n-i-1):
            # swap if element is greater
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# O( n log (n) ) average and worst case. Memory: Depends.
def merge_sort(arr):
    # each sub list will be sorted when merging
    if len(arr) > 1:
        mid = len(arr) // 2 # find middle
        l = arr[:mid] # create left array
        r = arr[mid:] # create right array
        merge_sort(l)
        merge_sort(r)
        i = j = k = 0
        # insert the smaller value between l[i] and r[j] at index k in arr
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        # fill remaining
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


def partition(arr, low, high):
    # pivot (element at right position)
    pivot = arr[high]
    i = low - 1 # all elements before index i is smaller than pivot value
    for j in range(low, high):
        # if current element is smaller than pivot
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


# runtime O(nlogn) average, O(n^2) worst case. Memeory O(logn)
def quick_sort(arr, low, high):
    if low < high:
        # partition index, arr[j] is now at right place
        pi = partition(arr, low, high)
        # seperate sort elements before partition and after partition
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


def insertion_sort(b):
    for i in range(1, len(b)):
        key = b[i]
        j = i - 1
        # continue moving key left until it is larger than current j index by shifting j to j+1
        while j >= 0 and b[j] > key:
            b[j+1] = b[j]
            j -= 1
        b[j+1] = key
    return b


def bucket_sort(x):
    arr = []
    slot_num = 10 # 10 slots, each slot size is 0.1
    for i in range(slot_num):
        arr.append([])

    # Put array elements in different buckets
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    # sort individual buckets
    for i in range(slot_num):
        arr[i] = insertion_sort(arr[i])

    # concat results
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x


# O(n^2) space O(1)
# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
# from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
def selection_sort(arr):
    i = 0
    while i < len(arr):
        low = i
        for j in range(i, len(arr)):
            if arr[j] < arr[low]:
                low = j
        arr[i], arr[low] = arr[low], arr[i]
        i += 1


if __name__ == '__main__':
    start1 = timeit.default_timer()
    arr1 = [52, 37, 63, 14, 17, 8, 6, 25]
    quick_sort(arr1, 0, len(arr1)-1)
    end1 = timeit.default_timer()
    print(arr1)
    print(end1 - start1)
    start2 = timeit.default_timer()
    arr2 = [52, 37, 63, 14, 17, 8, 6, 25]
    end2 = timeit.default_timer()
    print(end2 - start2)
    merge_sort(arr2)
    print(arr2)

    x = [0.897, 0.565, 0.656,
         0.1234, 0.665, 0.3434]
    print(bucket_sort(x))
    arr3 = [52, 37, 63, 14, 17, 8, 6, 25]
    selection_sort(arr3)
    print(arr3)