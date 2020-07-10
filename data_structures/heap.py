import heapq

# min-heap is a complete binary tree (totally filled other than the rightmost elements on the last level)
# where each node is smaller than its children. The root, is the min element in tree

# When we insert into a min-heap, we always start by inserting the element at the bottom. We insert at the
# rightmost spot so as to maintain the complete tree property.
# Then, we "fix" the tree by swapping the new element with its parent, until we find an appropriate spot for
# the element. We essentially bubble up the minimum element.

# Finding the minimum element of a min-heap is easy: it's always at the top. The trickier part is how to remove it.
# First, we remove the minimum element and swap it with the last element in the heap (the bottommost,
# rightmost element). Then, we bubble down this element, swapping it with one of its children until the minheap
# property is restored.
# Do we swap it with the left child or the right child? you'll need to take the smaller one in order to maintain
# the min-heap ordering.

# heapify: transform list x into heap,in-place, in linear time
# heappush: push item onto heap
# heappushpop: push item on heap pop and return smallest item from heap
# heapreplace: pop and return smallest item from heap and push the new item
if __name__ == '__main__':
    # priority queue using heapq
    x = [1,7,3,2,4]
    heapq.heapify(x)
    print(x)
    heapq.heappush(x, 5)
    heapq.heappush(x, 6)

    print(x)
    print(heapq.nlargest(1, x))
    print(heapq.nsmallest(1, x))
    while x:
        print(heapq.heappop(x))
