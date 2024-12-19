def soulution(n):
    tri = ''

    while n > 0:
        tri = str(n % 3) + tri
        n //= 3

    r-tri = tri[::-1]
    answer = int(r-tri, 3)

    return answer