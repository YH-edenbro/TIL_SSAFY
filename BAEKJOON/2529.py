# 백준 부등호

def dfs(index, total):
    global max_result, min_result

    if index == k + 1:
        num = ''.join(map(str, total))
        max_result = max(max_result, num)
        min_result = min(min_result, num)
        return

    for j in range(10):
        if selected[j]:
            continue
        if index == 0:
            selected[j] = 1
            dfs(index + 1, total + [j])
            selected[j] = 0
        elif budeung_list[index - 1] == '<' and total[-1] < j:
            selected[j] = 1
            dfs(index + 1, total + [j])
            selected[j] = 0
        elif budeung_list[index - 1] == '>' and total[-1] > j:
            selected[j] = 1
            dfs(index + 1, total + [j])
            selected[j] = 0



k = int(input())
budeung_list = list(input().split())
selected = [0] * 10
max_result = ''
min_result = '9999999999'
dfs(0, [])
print(max_result)
print(min_result)