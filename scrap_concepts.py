# ruff ignore I001, UP028
import csv
from datetime import datetime  # noqa: I001
from typing import Final, Self, Generator, Any  # noqa: UP035
from pathlib import Path
import sys

# number: int = 10
# decimal: float = 2.5
# text: str = "Hello world!"
# active: bool = False

# names: list = ["Bob", "Anna", "Luigi"]
# coordinates: tuple = (1.5, 2.5)
# unique: set = {1, 4, 2, 9}
# data: dict = {'name': 'Bob', 'age': 20}


# VERSION: Final[str] = '1.0.12'
# VERSION = '1.1' # error reported by type checker
# PI: Final[float] = 3.1415


# def show_date() -> None:
#     print('This is the current time:')
#     print(datetime.now())


# def greet(name: str) -> None:
#     print(f'Hello, {name}!')


# def add(a: float, b: float) -> float:
#     return a + b

class Car:
    def __init__(self, brand: str, hp: int) -> None:
        self.brand = brand
        self.hp = hp

    # def drive(self) -> None:
    #     print(f'{self.brand} is driving!')

    # def get_info(self) -> None:
    #     print(f"{self.brand} with {self.hp} horsepower")

    def __str__(self) -> str:
        return f"{self.brand}, {self.hp}hp"

    def __add__(self, other: Self) -> None:
        return f'{self.brand} & {other.brand}'


# generator 1
# def fibonacho_generator() -> Generator[int, None, None]:
#     """None of these values are being stored, they're being generated on the spot."""
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, (a + b)


# def main() -> None:
#     fib_gen: Generator[int, None, None] = fibonacho_generator()
#     n: int = 10
#     line_break: str = '-'*20

#     while True:
#         input(f'Tap "enter" for the next {n} numbers of fibonacci')
#         for i in range(n):
#             print(f"{next(fib_gen)}")

#         print(line_break)

# if __name__ == "__main__":
#     main()


# generator 2
# def read(path: str) -> Generator[str, None, str]:
#     with open(path) as file:
#         for line in file:
#             yield line.strip()

#     return 'This is the end!'


# def main() -> None:
#     reader: Generator[str, None, str] = read(Path('./note.txt'))
#     input('Press "Enter"')

#     while True:
#         try:
#             print(next(reader))
#         except StopIteration as e:
#             print('StopIteration:', e.value)
#             sys.exit()

#         input()

# if __name__ == "__main__":
#     main()

# generator 3
# def cum_sum() -> Generator[float, float, None]:
#     total: float = 0
#     while True:
#         # new_value: float = yield total
        # total += yield total

# def main() -> None:
#     cum_sum_generator: Generator[float, float, None] = cum_sum()
#     next(cum_sum_generator)
#     while True:
#         value: float = float(input('Enter a value: '))
#         current_sum: float = cum_sum_generator.send(value)
#         print(f'Cumulative sum: {current_sum}')

# if __name__ == "__main__":
#     main()

# generator 4
# def infinite_repeater(sequence: list[Any]) -> Generator[Any, None, None]:
#     while True:
#         for item in sequence:  # noqa: UP028
#             yield item


# def main() -> None:
#     repeater: Generator[Any, None, None] = infinite_repeater([1, 2, 3, 4])

#     for _ in range(10):
#         print(next(repeater))



# generator 5
def csv_row_reader(file_path: str) -> Generator[list[str], None, None]:
    with open(file_path) as csv_file:
        for row in csv.reader(csv_file):  # noqa: UP028
            yield row


def main() -> None:
    reader: Generator[list[str], None, None] = csv_row_reader('data.csv')

    while True:
        try:
            for i in range(3):
                print(next(reader))
            input('Continue retrieving rows?')
        except StopIteration:
            print('No more rows...')
            sys.exit()

if __name__ == "__main__":
    main()