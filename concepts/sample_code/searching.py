
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


def left_bisect_binary_search(self, array, target):  # bisect.bisect_left implementation
    lo = 0
    hi = len(array)

    while lo < hi:
        mid = (lo + hi) // 2
        if array[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


# greatest common denominator function
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Standard Kadane's algorithm to find maximum subarray sum
def kadane(a):
    n = len(a)
    max_so_far = a[0]
    max_ending_here = a[0]
    for i in range(1, n):
        max_ending_here = max(max_ending_here + a[i], a[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


# using bit masking to find all the combinations of characters in a string in lexicographical order of length k
# for a binary string of size n, a 1 at position i means that the combination contains characters[i]
# iterate from 0 to int(1*n) and get the binary where the number of 1s equal to k
def generate_combinations(characters, k):
    n = len(characters)
    end = int('1' * n, 2)
    res = []
    for i in range(end+1):
        b = bin(i)[2:]
        if b.count('1') == k:
            # map pos of 1 in bin to char in characters
            res.append(''.join(characters[j] if v == '1' else '' for j, v in enumerate(b.zfill(n))))
    return res

#TODO
# sequential recurrence relation and partition recurrence relation
# https://leetcode.com/problems/reverse-pairs/discuss/97268/General-principles-behind-problems-similar-to-%22Reverse-Pairs%22

if __name__ == '__main__':
    arr = [1, 4, 2, 5, 3, 7, 6]
    print(binary_search(arr, 4))
    print(binary_search_recursive(arr, 4, 0, len(arr)-1))
