import sys
input = sys.stdin.readline  # 빠른 입력
output = []

# 입력
num1 = int(input())
num2 = input().strip()  # 개행 문자 제거

sum = 0
for index, digit in enumerate(reversed(num2)):
    result = num1 * int(digit)
    output.append(str(result))
    digit_place_value = pow(10, index)
    sum += result * digit_place_value
    # sum += result * (10 ** i)

output.append(str(sum))

# 빠른 출력
sys.stdout.write('\n'.join(output) + '\n')
