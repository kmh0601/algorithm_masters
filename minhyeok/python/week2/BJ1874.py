# 1874 
# 스택 수열

# 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
# 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지

n = int(input()) # 1 <= n <= 100,000
nums = list(range(1,n+1))

target = []
stack = [0]

comb = []

for i in range(n):
    target.append(int(input()))

count = 0
i = 0
for x in target:
    if stack[-1] == x:
        comb.append('-')
        stack.pop()
        count += 1
        continue
    else:
        while i < n:
            if nums[i] == x:
                comb.append('+')
                comb.append('-')
                i += 1
                count += 1
                break
            else:
                comb.append('+')
                stack.append(nums[i])
                i += 1

if count == n:
    for k in comb:
        print(k)
else:
    print("NO")
