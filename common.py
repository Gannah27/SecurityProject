def text_to_numbers(text):
    """
    Convert text to ASCII numbers.
    """
    ascii_numbers =[]
    for char in text:
        ascii_numbers.append(ord(char))
    for index, value in enumerate(ascii_numbers):
        ascii_numbers[index] = str(ascii_numbers[index]- 27)
    return ''.join(ascii_numbers)

def numbers_to_text(numbers):
        number_str=str(numbers)
        split_numbers = [str(int(number_str[i:i + 2])+27) for i in range(0, len(number_str), 2)]
        print(split_numbers)
        text = ''.join(chr(int(num)) for num in split_numbers)
        return text