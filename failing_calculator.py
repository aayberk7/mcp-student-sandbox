from typing import Iterable


def average_ratios(numbers: Iterable[float]) -> float:
    """Return the average of 100 divided by each nonzero number.

    Raises ValueError if any input value is zero, since division by zero is undefined.
    """
    total = 0.0
    count = 0
    for index, value in enumerate(numbers):
        if value == 0:
            raise ValueError(f"Input value at index {index} is zero; cannot compute ratio")
        total += 100.0 / value
        count += 1

    if count == 0:
        raise ValueError("numbers must contain at least one nonzero value")

    return total / count


if __name__ == "__main__":
    print(average_ratios([10, 5, 0]))
