# 백준 1037번 / 약수

number = int(input())
num_list = list(map(int, input().split()))

if number <= 50:
    if number == len(num_list):
        print(max(num_list) * min(num_list))
