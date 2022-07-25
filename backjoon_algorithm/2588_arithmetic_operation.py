# 백준 2588번 / 사칙연산(*)

a = int(input())
b = input()

output_a = a * int(b[2])
output_b = a * int(b[1])
output_c = a * int(b[0])
output_d = a * int(b)

# sep= : 출력값이 여러 개일 경우 각 값 사이에 삽입할 문자를 지정하는 파라미터
print(output_a, output_b, output_c, output_d, sep="\n")
