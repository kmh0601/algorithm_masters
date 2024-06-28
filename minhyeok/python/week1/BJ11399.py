# 11399
# ATM

n = int(input())
nums = list(map(int, input().split(" ")))
nums.sort()

def ATM(nums):
    temp = 0
    result = 0
    for num in nums:
        temp += num
        result += temp
    return result
print(ATM(nums))
