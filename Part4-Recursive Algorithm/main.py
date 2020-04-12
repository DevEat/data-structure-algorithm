def solution(x):
    # Recursive version
    if x <= 1:
        return x

    return solution(x - 1) + solution(x - 2)


'''
def solution(x):
    # Iterative version
    if x <= 1:
        return x
    
    fibo = [0, 1]
    fibo = list(map(int, fibo))
    for idx in range(2, x + 1):
        fibo.append(fibo[idx - 1] + fibo[idx - 2])

    return fibo[x]
'''


def main():
    print(solution(11))


main()
