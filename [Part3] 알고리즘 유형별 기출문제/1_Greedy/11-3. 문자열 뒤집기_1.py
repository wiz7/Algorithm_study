data = input()

count_0 = 0
count_1 = 0

sub = data[0]

if sub != '1':
    count_0 = 1
else:
    count_1 = 1

for i in range(1, len(data)):
    if data[i] != sub and data[i] == '1':
        count_0 += 1
    elif data[i] != sub and data[i] == '0':
        count_1 += 1

    sub = data[i]

print(min(count_0, count_1))
