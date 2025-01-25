a = input()

b = a.strip()
c = b.split(sep= ' ')

if a == ' ':
    print(0)
else:    
    print(len(c))