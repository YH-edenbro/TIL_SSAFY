# 연산자 끼워넣기

def dfs(index, total):
    global max_result, min_result

    if index == N:
        max_result = max(max_result, total)
        min_result = min(min_result, total)
        return

    for i in range(4):
        if i == 0 and yeonsan[i] != 0:
            yeonsan[i] -= 1
            dfs(index + 1, total + num_list[index])
            yeonsan[i] += 1
        if i == 1 and yeonsan[i] != 0:
            yeonsan[i] -= 1
            dfs(index + 1, total - num_list[index])
            yeonsan[i] += 1
        if i == 2 and yeonsan[i] != 0:
            yeonsan[i] -= 1
            dfs(index + 1, total * num_list[index])
            yeonsan[i] += 1
        if i == 3 and yeonsan[i] != 0 and num_list[index] != 0:
            if total >= 0:
                yeonsan[i] -= 1
                dfs(index + 1, total // num_list[index])
                yeonsan[i] += 1
            elif total < 0:
                yeonsan[i] -= 1
                dfs(index + 1, -(-total // num_list[index]))
                yeonsan[i] += 1


N = int(input())
num_list = list(map(int, input().split()))
yeonsan = list(map(int, input().split()))
max_result = -1000000001
min_result = 1000000001
dfs(1, num_list[0])
print(max_result)
print(min_result)