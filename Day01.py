from advent_util import get_file_data

number = get_file_data("input_file")[0]

part_two_step = int(len(number) / 2)

part_one_answer = 0
for i in range(0, len(number)):
    check_index = i+1
    if check_index > len(number)-1:
        check_index = 0
    if number[i] == number[check_index]:
        part_one_answer += int(number[i])

print("Part one answer:", part_one_answer)

part_two_answer = 0

for i in range(0, len(number)):
    check_index = i+part_two_step
    if check_index > len(number)-1:
        check_index = check_index - len(number)
    if number[i] == number[check_index]:
        part_two_answer += int(number[i])

print("Part two answer:", part_two_answer)
