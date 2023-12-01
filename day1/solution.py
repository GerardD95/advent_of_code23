import re 

# read data from file
def read_data(file_name):
    with open(file_name, 'r') as f:
        data = f.readlines()
    return data

data = read_data('data/input.txt')

# Part1
def part1(data):
  only_numbers = [[char for char in text_str if char.isdigit()] for text_str in data]
  return [int(f"{i[0]}{i[-1]}") for i in only_numbers]

# Part2
def part2(text):
  # Define a mapping for the words to their numerical representations
  number_mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
  }
  
  char_index = 0
  while char_index <= len(text):
    for key, value in number_mapping.items():
      text_selection = text[char_index:char_index + len(key)]
      if text_selection == key:
        text = text.replace(text_selection, value)
        char_index += 1
        break
      # check if key value pair is the lat in number_mapping
      elif key == list(number_mapping.keys())[-1]:
        char_index += 1
  
  return text


data = [
  # 'two1nine',
  'eightwothree',
  # 'abcone2threexyz',
  # 'xtwone3four',
  # '4nineeightseven2',
  # 'zoneight234',
  # '7pqrstsixteen'
]

# Convert written numbers to digits
res = [part2(line) for line in data]
with open("data/output.txt", "w") as f:
  for line in res:
    f.write(f"{line}")

with open("data/numbers.txt", 'w') as f:
  for line in part1(res):
    f.write(f"{line}\n")

# get all numbers from text
num_lst = part1(res)

# sum all numbers
print(res)
print(f"Sum of all numbers: {sum(num_lst)}")
