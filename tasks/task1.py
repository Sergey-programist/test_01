numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
text = "Hello, World!"


def sum_all_elements(numbers: list) -> int:
    result = 0
    for element in numbers:
        result += element
    return result


def multiply_all_elements(numbers: list) -> int:
    result = 1
    for element in numbers:
        result *= element
    return result


def reverse_string(text: str) -> str:
    buffer = ""
    for element in text:
        buffer = element + buffer
    return buffer


a = sum_all_elements(numbers)
b = multiply_all_elements(numbers)
c = reverse_string(text)

print(a, b, c)
