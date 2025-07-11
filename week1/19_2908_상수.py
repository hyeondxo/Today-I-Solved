a, b = input().split()
r_a = ''.join(reversed(a))
r_b = ''.join(reversed(b))
print(max(int(r_a), int(r_b)))
