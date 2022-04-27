"""
Write a function with one parameter of type string, that returns a list containing the characters of the parameter.
If a character in the string is a space or a digit greater than 5, remove them and do not include them in the array.
"""


def str_to_list(param: str) -> list[str]:
    """Convert a string to list of characters with a special rule."""

    assert isinstance(param, str)

    prohibited_symbols = (' ', '6', '7', '8', '9')

    return [char for char in param if char not in prohibited_symbols]


test_cases = {
    'abc123': ['a', 'b', 'c', '1', '2', '3'],
    'abc123 ': ['a', 'b', 'c', '1', '2', '3'],
    'abc1236': ['a', 'b', 'c', '1', '2', '3'],
    '': [],
    '  ': [],
    '6789': [],
}

for input_data, estimate_result in test_cases.items():
    result = str_to_list(input_data)
    assert str_to_list(input_data) == estimate_result, f'{result} != {estimate_result}'
