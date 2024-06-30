# 18114
# 블랙 프라이데이

n, c = map(int,input().split(" "))
weights = list(map(int, input().split(" ")))
weights.sort()

def blackFriday(weights, c):
    if c in weights:
        return True
    
    i = 0
    j = n - 1
    while (i < j):
        if weights[i] + weights[j] == c:
            return True
        elif weights[i] + weights[j] > c:
            j -= 1
            continue
        else: # weights[i] + weights[j] < c
            if (c - weights[i] - weights[j]) in weights[i+1:j]:
                return True
            else:
                i += 1
    return False

if blackFriday(weights, c):
    print(1)
else: 
    print(0)