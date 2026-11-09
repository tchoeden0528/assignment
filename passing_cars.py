# PassingCars
# 0 = car going east, 1 = car going west
# count how many pairs of cars pass each other

def solution(A):
    east_cars = 0
    passing = 0

    for car in A:
        if car == 0:
            # another east car
            east_cars = east_cars + 1
        else:
            # this west car passes every east car that came before it
            passing = passing + east_cars

    # the problem says to return -1 if the number is too big
    if passing > 1000000000:
        return -1

    return passing

print(solution([0, 1, 0, 1, 1]))  # should be 5
