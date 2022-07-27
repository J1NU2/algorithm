# 백준 1157번 / 단어 공부

# upper() : 모든 알파벳 대문자로 변경(= lower() : 소문자)
# set() : 자료형에서 중복값을 제거, 순서가 없음
# count() : 문자열 내에서 찾고자 하는 특정 문자의 개수
# max() : 가장 값이 큰 것을 반환
# index() : 리스트에서 찾고자 하는 요소를 찾기, 중복x

word = input().upper()
word_list = list(set(word))
word_count = []

print(word)
print(word_list)

for i in word_list:
    a = word.count(i)
    word_count.append(a)

print(word_count)

if word_count.count(max(word_count)) >= 2:
    print("?")
else:
    print(word_list[(word_count.index(max(word_count)))])
