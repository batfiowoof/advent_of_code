import re

text = input()
total_sum = 0

while text:

    pattern = r'\d'
    numbers = re.findall(pattern, text)
    nums_together = numbers[0] + numbers[-1]
    total_sum += int(nums_together)
    text = input()

print(total_sum)