# 백준 1316번 / 그룹 단어 체커

# for _ in range() : 해당 인덱스 무시

count = int(input())
group_word = count

for _ in range(count):
    word = input()

    for i in range(0, len(word) - 1):
        if word[i] == word[i + 1]:
            pass
        elif word[i] in word[i+1:]:
            group_word -= 1
            break

print(group_word)
