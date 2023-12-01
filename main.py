import re

with open("calibration.txt", "r") as file:
    calibration_list: list = file.read().split('\n')

def preprocessor(string_combo_input: str) -> int:
    string_numbers: list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    new_string: str = string_combo_input
    numbers_list: list = []
    # Looping through the string
    for character_index, character in enumerate(new_string):
        if character.isdigit(): # If the character in the string is digit we append it to the numbers list.
            numbers_list.append(character)
        # looping through the values in our string numbers list
        for value_index, value in enumerate(string_numbers):
            if new_string[character_index:].startswith(value): # we start checking from the current character index slice if is start with any of the numbers on it
                numbers_list.append(str(value_index + 1)) # If it starts with the number we append it to the list.
   
    return int(str(numbers_list[0] + numbers_list[-1]))
            

digits_total: int = 0

for combination in calibration_list:
    int_digits: int = preprocessor(combination)
    digits_total += int_digits

print(digits_total)
