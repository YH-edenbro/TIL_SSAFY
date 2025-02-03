T = int(input())
 
for test_case in range(1, T+1):
    a = list(map(int, input().split()))
    b = []
     
    for item in a:
        if item % 2 != 0:
            b.append(item)
    print(f"#{test_case} {sum(b)}")