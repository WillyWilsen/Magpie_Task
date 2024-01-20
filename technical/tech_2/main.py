# Input
input = input()

# Process
numbers = []
for i in range(len(input)):
  if input[i] == '5':
    print(input[:i] + input[i+1:])
    numbers.append(int(input[:i] + input[i+1:]))

# Output
print(min(numbers))