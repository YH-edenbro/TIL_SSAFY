# 바구니 뒤집기

def reverse_basket(a, b, arr):
    ans = []
    if a > 0:
        for idx in range(0, a):
            ans.append(arr[idx])
    for idx in range(b, a-1, -1):
        ans.append(arr[idx])
    if b < N:
        for idx in range(b+1, N):
            ans.append(arr[idx])
    return ans


N, M = map(int, input().split())
basket = list(range(1, N+1))
for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    basket = reverse_basket(i, j, basket)

print(' '.join(map(str, basket)))
