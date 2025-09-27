import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
num = a * b * c

output = [0 for _ in range(10)]
# output = [0] * 10

# num = str(a * b * c)
# count = Counter(num) 문자열 내 각 문자의 개수를 딕셔너리 형태로 반환
# ex - ({'0': 1, '1': 4, '2': 3})

# for i in range(10):
#   print(count.get(str(i), 0)) # 키(숫자)를 통해 해당 숫자의 개수 조회

for i in str(num):
    output[int(i)] += 1

for total_count in output:
    print(total_count)
