# 백준 4344번 / 평균은 넘겠지

case_cnt = int(input())

# for _ in range() : 해당 인덱스 무시
for _ in range(case_cnt):
    scores = list(map(int, input().split()))
    average = sum(scores[1:]) / scores[0]
    count = 0

    for score in scores[1:]:
        if score > average:
            count += 1

    # percent = round((count / scores[0]) * 100, 3)
    percent = (count / scores[0]) * 100
    print(f"{percent:.3f}%")
