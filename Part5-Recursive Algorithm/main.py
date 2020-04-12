def solution(bin, x, l, r):
    if l > r:
        return -1

    mid = (l + r) // 2
    if x == bin[mid]:
        return mid
    elif x < bin[mid]:
        return solution(bin, x, l, mid - 1)
    else:
        return solution(bin, x, mid + 1, r)


def main():
    bin = list(map(int, [2, 4, 5, 7, 9, 11]))
    x = 6
    print(solution(bin, x, 0, len(bin)))


main()