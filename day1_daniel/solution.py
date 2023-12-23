def read_data(path):
    with open(path, 'r') as f:
        data = f.read().split("\n")
        return data

path = 'data/input.txt'
data = read_data(path)

lines_to_numbers = []
for line in data:
    line_numbers = []
    for char in line:
        if char.isdigit():
            line_numbers.append(char) 
    lines_to_numbers.append(line_numbers)


lines_to_numbers = [int(f"{line[0]}{line[-1]}") for line in lines_to_numbers]
print(sum(lines_to_numbers))

