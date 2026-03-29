def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    :param numbers: list of numeric values
    :return: float average value
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")

    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("All elements must be int or float")

    total = sum(numbers)
    count = len(numbers)

    return total / count


def group_by_length(strings):
    """
    Groups strings based on their length.
    """
    if not isinstance(strings, list):
        raise TypeError("Input must be a list")

    result = {}
    for s in strings:
        if isinstance(s, str):
            length = len(s)
            result.setdefault(length, []).append(s)

    return result

