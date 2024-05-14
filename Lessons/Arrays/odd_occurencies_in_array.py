# Brute force Method
# Complexity 0(N ** 2)
def brute(A):
    N = len(A)
    answer = 0
    for i in range(N):
        if A.count(A[i]) % 2 != 0:
            answer =  A[i]
            break
    return answer

# Complexity 0(N)
def solution(A):
    appearance = dict()
    for i in A:
        appearance[i] = appearance.get(i, 0) + 1
    for i, count in appearance.items():
        if count % 2 != 0:
            return i
    return None

a  = [9,3,9,3,9,7,9]

print(solution(a))
        