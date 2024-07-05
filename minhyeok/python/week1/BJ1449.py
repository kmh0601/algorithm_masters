# 1449
# 수리공 항승

n, l = map(int, input().split(" "))
pipes = list(map(int, input().split(" ")))
pipes.sort()

count = 0
i = 0
while i < n:
    start = pipes[i]
    # print(start, "의 물을 막기 시작함!")
    for j in range(i, n):
        if pipes[j] - start >= l:
            break
        # print(pipes[j], "의 물도 막음")
        i += 1
    count += 1

print(count)
# l 길이의 테이프로는 한 번에 l-1 만큼 연속한 갯수의 파이프의 물을 막을 수 있다