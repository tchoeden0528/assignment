# TapeEquilibrium
# split the list into two parts and find the smallest difference between their sums

def solution(A):
    total = sum(A)
    left_sum = 0
    smallest = None

    # try every place we can split (can't split before the first or after the last)
    for p in range(1, len(A)):
        left_sum = left_sum + A[p - 1]
        right_sum = total - left_sum
        diff = abs(left_sum - right_sum)

        if smallest is None or diff < smallest:
            smallest = diff

    return smallest

print(solution([3, 1, 2, 4, 3]))  # should be 1
