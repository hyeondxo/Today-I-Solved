import sys
input = sys.stdin.readline

score = int(input()) // 10

output = ""

if (score >= 9):
    output = "A"
elif (score == 8):
    output = "B"
elif (score == 7):
    output = "C"
elif (score == 6):
    output = "D"
else:
    output = "F"

sys.stdout.write(output + "\n")
