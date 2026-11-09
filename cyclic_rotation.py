# CyclicRotation
# moves every element one spot to the right, K times

def solution(A, K):
    # if the list is empty there is nothing to rotate
    if len(A) == 0:
        return A

    # rotating len(A) times gets you back to the start, so skip those
    K = K % len(A)

    for i in range(K):
        last = A.pop()      # take the last number off
        A.insert(0, last)   # put it at the front

    return A

print(solution([3, 8, 9, 7, 6], 3))  # should be [9, 7, 6, 3, 8]
print(solution([1, 2, 3, 4], 4))     # should be [1, 2, 3, 4]
