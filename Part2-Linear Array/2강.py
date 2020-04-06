def solution_first(L, x):
    answer = []

    if x < L[0]:
        L.insert(0, x)
    elif L[-1] < x:
        L.insert(len(L), x)
    else:
        for idx in range(len(L)):
            if L[idx] < x and x < L[idx + 1]:
                L.insert(idx + 1, x)
                break

    answer = L
    return answer


def solution_second(L, x):
    answer = []

    for idx, val in enumerate(L):
        if x == val:
            answer.append(idx)

    if 0 == len(answer):
        answer.append(-1)

    return answer


def main():
    L1 = [20, 37, 58, 72, 91]
    x1 = 65
    answer_first = solution_first(L1, x1)
    print(answer_first)

    L2 = [64, 72, 83, 72, 54]
    x2 = 72
    answer_second = solution_second(L2, x2)
    print(answer_second)

main()
