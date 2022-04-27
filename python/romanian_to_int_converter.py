"""
Write a function to convert Roman numerals to integers.
"""

# Solution 1
# Just install and use the external package like https://github.com/zopefoundation/roman


# Solution 2
def convert(param: str) -> int:
    """Convert a romanian number to int."""
    romanians = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    # TODO: check that the input param is a valid Romanian number (symbols order conditions)
    assert set(param).issubset({'I', 'V', 'X', 'L', 'C', 'D', 'M'})

    n = len(param)
    result = 0
    i = 0

    while i < n:

        if i + 1 < n and romanians[param[i]] < romanians[param[i + 1]]:
            result += romanians[param[i + 1]] - romanians[param[i]]
            i += 1

        else:
            result += romanians[param[i]]

        i += 1

    return result


test_cases = {
    'I': 1,
    'III': 3,
    'IV': 4,
    'IX': 9,
    'XIV': 14,
    'XIX': 19,
    'XXIV': 24,
    'XL': 40,
    'XLIX': 49,
    'XC': 90,
    'XCIX': 99,
    'CD': 400,
    'CDXC': 490,
    'CDXCIX': 499,
    'CM': 900,
    'CMXC': 990,
    'CMXCVIII': 998,
    'CMXCIX': 999,
    'MMXIII': 2013,
    'MMMCMXCIX': 3999,
}

for input_data, estimate_result in test_cases.items():
    result = convert(input_data)
    assert result == estimate_result, f'{result} != {estimate_result}'
