from typing import Iterable, List, Sequence

LOG_FILE_PATH = "log.txt"


def calculate_total(value: float, rate: float = 0.15) -> float:
    """Return a value after applying a percentage increase."""
    return value * (1 + rate)


def format_total(value: float) -> str:
    """Format a processed total for display."""
    return f"Total: {value:.2f}"


def append_log(values: Sequence[float], path: str = LOG_FILE_PATH) -> None:
    """Append processed values to a log file."""
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{list(values)}\n")


def display_results(results: Sequence[float]) -> None:
    """Print formatted totals to standard output."""
    for total in results:
        print(format_total(total))


def process_data(data: Iterable[float], rate: float = 0.15) -> List[float]:
    """Process numeric input values and return their updated totals."""
    return [calculate_total(value, rate) for value in data]


def main() -> None:
    sample_data = [100.0, 200.0, 50.5]
    results = process_data(sample_data)
    display_results(results)
    append_log(results)


if __name__ == "__main__":
    main()
