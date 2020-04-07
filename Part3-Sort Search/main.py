def solution(L, x):
    answer = -1

    l = 0
    r = len(L) - 1
    m = int((l + r) / 2)

    while l <= r:
        if L[m] == x:
            answer = m
            break

        if x < L[m]:
            r = m - 1
            m = int((l + r) / 2)

        if L[m] < x:
            l = m + 1
            m = int((l + r) / 2)

    return answer


def main():
    L = [2, 5, 7, 9, 11]
    x = 5

    idx = solution(L, x)
    print(idx)


main()
