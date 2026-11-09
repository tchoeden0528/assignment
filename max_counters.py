# MaxCounters
# N counters start at 0
# if X is between 1 and N, add 1 to counter X
# if X is N + 1, set all counters to the biggest counter

def solution(N, A):
    counters = [0] * N
    biggest = 0       # biggest counter so far
    reset_value = 0   # what all counters got set to last time

    # setting every counter each time is too slow,
    # so we just remember reset_value and fix counters when we use them

    for X in A:
        if X >= 1 and X <= N:
            index = X - 1   # lists start at 0

            # if this counter is behind the last reset, catch it up
            if counters[index] < reset_value:
                counters[index] = reset_value

            counters[index] = counters[index] + 1

            if counters[index] > biggest:
                biggest = counters[index]
        else:
            reset_value = biggest

    # catch up any counters that never got touched after the last reset
    for i in range(N):
        if counters[i] < reset_value:
            counters[i] = reset_value

    return counters

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))  # should be [3, 2, 2, 4, 2]
