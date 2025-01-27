s = input()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
index_num = []
for char in alphabet:
    if char not in s:
        index_num.append(-1)
    else:
        index_num.append(s.index(char))

print(*index_num) 