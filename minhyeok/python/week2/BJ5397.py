# 5397
# 키로커

T = int(input())
strings = []
for i in range(T):
    strings.append(input())
index = 0
while index < T:
    string = strings[index]
    stack = []
    temp = []
    for char in string:
        if char == '<':
            if stack:
                temp.append(stack.pop())
        elif char == '>':
            if temp:
                stack.append(temp.pop())
        elif char == '-':
            if stack:
                stack.pop()
        else:
            stack.append(char)
    if temp:
        stack = stack + temp[::-1]
    print(''.join(stack))
    index += 1