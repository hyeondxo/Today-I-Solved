import sys
input = sys.stdin.readline  # 빠른 입력
output = []

# 입력
num1 = int(input())
num2 = input().strip()  # 개행 문자 제거

# 두 번째 수를 뒤에서부터 순회
# 실제 자리수의 값 계산 - 10을 index만큼 제곱하는 방법
# 이 때 index는 실제 index가 아닌 0부터 시작
# 자리수와 자리수 값을 곱하여 실 곱셈 자리수 값 계산
sum = 0
for index, digit in enumerate(reversed(num2)):
    result = num1 * int(digit)
    output.append(str(result))
    digit_place_value = pow(10, index)
    sum += result * digit_place_value

output.append(str(sum))

# 빠른 출력
sys.stdout.write('\n'.join(output) + '\n')
