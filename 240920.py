def solution(n):

    def hanoi(s, e, t, N):
        if N == 1:
            return[[s, e]]
        return hanoi(s, t, e, N-1) + [[s, e]] + hanoi(t, e, s, N-1)
    
    return hanoi(1, 3, 2, n)