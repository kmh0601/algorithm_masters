# 2548
# 대표 자연수

n = int(input())
nums = list(map(int, input().split(" ")))
nums.sort()

# 찬찬히 생각해보니 그냥 중앙값을 구하는 문제
def median(n, nums):
    result = None
    if n % 2 == 0:
        result = nums[n//2 - 1]
    else:
        result = nums[n//2]
    return result

print(median(n, nums))