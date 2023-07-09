with open('input.txt', 'r') as f:
    content = f.readline()
print(content, type(content))
total_1 = 0
total_2 = 0
pos = 1

for f in content:
    if f == '(':
        total_1 += 1
    elif f == ')':
        total_1 -= 1

for f in content:
    if f == '(':
        total_2 += 1
    elif f == ')':
        total_2 -= 1
    if total_2 == -1:
        break
    pos += 1

print(total_1)
print(pos)
