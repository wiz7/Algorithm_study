input_data = list(map(int, str(input())))

left_value = sum(input_data[0:int(len(input_data) / 2)])
right_value = sum(input_data[int(len(input_data) / 2):])

if left_value == right_value:
    print('LUCKY')
else:
    print('READY')
