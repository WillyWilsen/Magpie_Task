# Input
input = input()

# Process
numbers = input.split()
numbers = [int(num) for num in numbers]
start_period = numbers[0]
output = 0
for i in range(1, len(numbers)):
  if numbers[i] < start_period:
    output = i
    break

# Output
print(output)