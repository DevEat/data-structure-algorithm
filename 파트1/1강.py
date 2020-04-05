import time


def solution(data):
    return data[0] + data[-1] # start, end of list


def checkTime():
    n = int(input("Number of elements : "))
    stack = [k for k in range(n)]

    print("Searching for the maximum value ...")

    start = time.time()
    maximum = max(stack)
    end = time.time()

    print("Maximum element = %d, End time = %.2f" % (maximum, end-start))


def main():
    #checkTime()

    data = list(map(int, input("data : ").split()))

    sum = solution(data)
    print(sum)


main()

# 내가 어떤 자료구조를 택해서 어떤 문제를 풀것이냐.
# 풀어야 하는 문제가 어떤 것인데 그러면 내가 풀어야하는 문제는 어떤 자료구조를 택해야하는가

# 알고리즘이란 ?
# 어떤 문제를 해결하기 위한 절차, 방법, 명령어들의 집합
# 주어진 문제의 해결을 위한 자료구조와 연산 방법에 대한 선택
