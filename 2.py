import re

text = input()
total_sum = 0

word_nums = {'one': 'o1e',
             'two': 't2o',
             'three': 'tr3e',
             'four': 'f4r',
             'five': 'f5e',
             'six': 's6x',
             'seven': 's7en',
             'eight': 'e8ght',
             'nine': 'n9ne'}

while text:
    for key, value in word_nums.items():
        text = text.replace(key, value)

    pattern = r'\d'
    numbers = re.findall(pattern, text)
    nums_together = numbers[0] + numbers[-1]
    total_sum += int(nums_together)
    text = input()

print(total_sum)
