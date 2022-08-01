# 백준 2609번 / 최대공약수와 최소공배수

a, b = map(int, input().split())
max_num, min_num = max(a, b), min(a, b)

while min_num > 0:
    max_num, min_num = min_num, max_num % min_num

print(max_num)
print((a * b) // max_num)

# python math 모듈 사용
# import math
# a_num, b_num = map(int, input().split())
# print(math.gcd(a_num, b_num))  # 최대공약수
# print(math.lcm(a_num, b_num))  # 최소공배수
