# 2470
# 두 용액
import math

n = int(input())
nums = list(map(int, input().split(" ")))

nums.sort()

divMin = math.inf
comb = []

i = 0
j = n-1
while i < j:
    div = nums[i] + nums[j]
    if divMin > abs(div):
        divMin = abs(div)
        comb = [i,j]
    if div > 0:
        j -= 1
    else:
        i += 1

print(nums[comb[0]], nums[comb[1]])
