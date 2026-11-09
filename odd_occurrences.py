# OddOccurrencesInArray
# every number has a pair except one, find the one without a pair

def solution(A):
    counts = {}

    # count how many times each number shows up
    for num in A:
        if num in counts:
            counts[num] = counts[num] + 1
        else:
            counts[num] = 1

    # the answer is the number that shows up an odd number of times
    for num in counts:
        if counts[num] % 2 == 1:
            return num

print(solution([9, 3, 9, 3, 9, 7, 9]))  # should be 7
