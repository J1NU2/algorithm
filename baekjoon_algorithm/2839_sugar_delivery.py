# 백준 2839번 / 설탕 배달

# 5로 딱 나눠 떨어질 경우 : 나눈 값의 몫(정수) 저장
# 5로 딱 나눠 떨어지지 않는 경우 : 입력 값을 3씩 줄이고 1씩 저장, 반복
# 5 또는 3 으로도 나눠 떨어지지 않는 경우 : -1 반환

weight = int(input())
sugar = 0

while True:
    if (weight % 5) == 0:
        sugar += (weight // 5)
        print(sugar)
        break

    weight -= 3
    sugar += 1

    if weight < 0:
        print("-1")
        break
