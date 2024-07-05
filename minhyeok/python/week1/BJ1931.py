# 1931
# 회의실 배정

n = int(input())
meetings = []

for i in range(n):
    temp = tuple(map(int, input().split(" ")))
    meetings.append(temp)

# 튜플의 두 번째 값으로 정렬(끝나는 시간이 이른 순서로 정렬)
meetings.sort(key = lambda x : (x[1], x[0]))

point = 0
count = 0
for start, end in meetings:
    if point <= start:
        count += 1
        point = end

print(count)