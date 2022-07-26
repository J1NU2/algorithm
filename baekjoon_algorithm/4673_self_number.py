# 백준 4673번 / 셀프 넘버

# set() : 자료형에서 중복값 제거, 교집합/합집합/차집합을 구할 때 사용
numbers = set(range(1, 10000))
set_number = set()

for number in numbers:
    for num in str(number):
        number += int(num)
    set_number.add(number)

self_numbers = numbers - set_number

# sorted() : 정렬 내장함수, 리스트를 정렬하여 새로운 리스트 반환
for self_num in sorted(self_numbers):
    print(self_num)
