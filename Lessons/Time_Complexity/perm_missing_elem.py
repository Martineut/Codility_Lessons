def solution(A):
    N = len(A)
    total_sum = ((N + 1) * (N + 2)) // 2
    sum_of_list = sum(A)
    return total_sum - sum_of_list

a = [2,3,1,5,6]
print(solution(a))