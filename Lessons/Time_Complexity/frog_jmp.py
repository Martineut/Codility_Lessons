import math
# Brute force method
# Complexity is O(Y - X)
def brute(X,Y,D):
    number_of_loops = 0
    for i in range(X, Y, D):
        number_of_loops += 1
    return number_of_loops


def solution(X, Y, D):
    answer = (Y-X)/D
    return math.ceil(answer)


print(brute(10, 85, 30))