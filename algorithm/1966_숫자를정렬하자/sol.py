import sys
sys.stdin = open('input (2).txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr =list(map(int, input().split()))
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    result = ' '.join(list(map(str, arr)))

    print("#{} {}".format(tc, result))