input_data = list(map(str, str(input())))

alphabet_list = []
number_value = 0

for i in input_data:
    if i.isdigit():
        number_value += int(i)
    else:
        alphabet_list.append(i)

print(''.join(sorted(alphabet_list))+str(number_value))
