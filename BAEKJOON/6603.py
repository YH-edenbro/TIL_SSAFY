# 로또

def dfs(index, lotto):
    if len(lotto) > 6:
        return

    if index == k:
        if len(lotto) == 6:
            print(f"{' '.join(map(str, lotto))}")
            return
        else:
            return

    dfs(index + 1, lotto + [s[index]])

    dfs(index + 1, lotto)


while True:
    k_list = list(map(int, input().split()))
    if k_list == [0]:
        break
    k = k_list[0]
    s = k_list[1:k+1]
    visited = [0] * k
    dfs(0, [])
    print('')