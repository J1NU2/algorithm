# 백준 2941번 / 크로아티아 알파벳

# replace() : 현재 문자열을 지정된 새로운 문자열로 바꿔주는 함수

word = input()
croatia_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for change in croatia_alphabet:
    word = word.replace(change, "c")

print(len(word))
