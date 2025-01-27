string = list(input().upper())
string.sort()

unique_list   = []
count_list = []

for char in string:
    if char not in unique_list:
        unique_list.append(char)

for char in unique_list:
    count_list.append(string.count(char))

if count_list.count(max(count_list)) >= 2:
    print('?')
else:
    print(unique_list[count_list.index(max(count_list))])