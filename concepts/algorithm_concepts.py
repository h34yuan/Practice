from collections import Counter


# presum and sliding window to find subarrays with sum S
def numSubarraysWithSum(self, A, S) -> int:
    c = Counter({0: 1})
    psum = res = 0
    for i in A:
        psum += i
        res += c[psum - S]
        c[psum] += 1
    return res

# int to binary string
def int_to_bin(s):
    # {} place a variable into a string
    # 0 takes variable at arg pos 0
    # : adds formatting option
    # 0n formats num to n digit zero padding on left
    # b converts to binary representation
    return"{0:b}".format(s)