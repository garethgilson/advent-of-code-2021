import fileinput

depth = 0
position = 0

print("Starting program...")

with fileinput.input(files='input/20211202-dive.txt') as input:
    for line in input:
      instruction = line.split(' ')
      if instruction[0] == 'forward':
        position += int(instruction[1])
      elif instruction[0] == 'down':
        depth += int(instruction[1])
      elif instruction[0] == 'up':
        depth -= int(instruction[1])

print('### PART ONE ###')
print('Position: ' + str(position))
print('Depth: ' + str(depth))
print('Result: ' + str(position*depth))

depth = 0
position = 0
aim = 0

with fileinput.input(files='input/20211202-dive.txt') as input:
    for line in input:
      instruction = line.split(' ')
      if instruction[0] == 'forward':
        position += int(instruction[1])
        depth += int(instruction[1]) * aim
      elif instruction[0] == 'down':
        aim += int(instruction[1])
      elif instruction[0] == 'up':
        aim -= int(instruction[1])

print('### PART TWO ###')
print('Position: ' + str(position))
print('Depth: ' + str(depth))
print('Result: ' + str(position*depth))