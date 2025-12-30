def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("input_file")
number_lists = []

for line in file_data:
    number_lists.append([int(x) for x in line.split()])

part_one_answer = 0
part_one_answer += sum(max(numbers) - min(numbers) for numbers in number_lists)

print("Part one answer:", part_one_answer)

part_two_answer = 0

part_two_answer += sum(int(n1 / n2) for number in number_lists for n1 in number for n2 in number
                       if n1 != n2 and n1 % n2 == 0)

print("Part two answer:", part_two_answer)

