data = input()
result = 0

for i in range(len(data)):
    sub = int(data[i])
    if result == 0 or sub == 0:
        result += sub
    else:
        result *= sub

print(result)
