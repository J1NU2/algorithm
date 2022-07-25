# 백준 2884번 / 알람 시계

hour, minute = map(int, input().split())

if minute < 45:
    minute += 15
    hour -= 1
    if hour < 0:
        hour = 23
else:
    minute -= 45

print(hour, minute)
