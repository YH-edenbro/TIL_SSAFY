T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.



for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    list_y = []
    list_x = []


    if n > m:
        list_b = b
        for i in range(n - m + 1):
            list_a = a[i:i+m]
            for j in range(m):
                x = list_a[j] * list_b[j]
                list_x.append(x)
            list_y.append(sum(list_x))
            list_x = []
        print(f"#{test_case} {max(list_y)}")

    elif n == m:
        for num1, num2 in zip(a,b):
            x = num1 * num2
            list_x.append(x)
            list_y.append(sum(list_x))
        print(f"#{test_case} {max(list_y)}")

    else:
        list_a = a
        for i in range(m - n + 1):
            list_b = b[i:i + n]
            for j in range(n):
                x = list_a[j] * list_b[j]
                list_x.append(x)
            list_y.append(sum(list_x))
            list_x = []
        print(f"#{test_case} {max(list_y)}")
