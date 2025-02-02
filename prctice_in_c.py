list_a = []

for i in range(9):
    a = list(map(int, input().split()))
    list_a.extend(a)


max_a = max(list_a)
max_a_index = list_a.index(max_a)
row = max_a_index // 9 + 1
col = max_a_index % 9 + 1

print(max_a)
print(row, col)