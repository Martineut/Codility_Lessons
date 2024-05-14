def solution(A, K):
    N = len(A)
    if N == 0:
        return A
    else:
        J = K % N
        rotated_list = [0] * N
        for i in range(N):
            if K <= N:
                rotated_list[i] = A[(i - (K + 1)) + 1]
            else:
                rotated_list[i] = A[(i - (J + 1)) + 1]
    return rotated_list
a = []
print(solution(a, 121))