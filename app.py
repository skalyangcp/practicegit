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


# Example usage
if __name__ == "__main__":
    data = [10, 20, 30, 40]
    avg = calculate_average(data)
    print(f"Average: {avg}")
