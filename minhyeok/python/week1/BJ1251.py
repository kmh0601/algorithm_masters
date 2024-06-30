# 1251
# 단어 나누기

word = input()
newWord = 'z'*50

for i in range(1, len(word)):
    for j in range(i+1, len(word)):
        part1 = word[0:i][::-1]
        part2 = word[i:j][::-1]
        part3 = word[j:][::-1]
        temp = part1+part2+part3
        newWord = temp if temp < newWord else newWord

print(newWord)
