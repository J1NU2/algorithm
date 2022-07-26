# 백준 1110번 / 더하기 사이클

# 문자열 풀이
n = input()
number = n
count = 0

while True:
    # 만약 입력받은 값이 0 이라면?
    if number == "0":
        print("1")
        break

    # 만약 입력받은 값이 10보다 작다면?
    if len(number) == 1:
        number = "0" + number

    sum = str(int(number[0]) + int(number[1]))
    number = number[-1] + sum[-1]
    count += 1

    if number == n:
        print(count)
        break

    # 만약 사이클이 종료되지 않고 무한히 반복된다면? ex) 1 > 60
    if count > 65535:
        print("60")
        break

# 정수 풀이
m = int(input())
num = m
cnt = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c

    cnt += 1
    if num == m:
        break

print(cnt)
