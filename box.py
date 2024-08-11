from dataclasses import dataclass, field  # noqa: INP001
from typing import Self


@dataclass()
class Fruit:
    name: str
    volume: float


class BoxFullError(Exception):
    def __init__(self, fruit: Fruit) -> None:
        super().__init__(f"Can't add {fruit.name} to the box as it is full")


@dataclass(slots=True)
class Box:
    capacity: float
    fruits: list[Fruit] = field(init=False)

    def __post_init__(self) -> None:
        self.fruits = []

    @property
    def volume(self) -> float:
        return sum(fruit.volume for fruit in self.fruits)

    def __str__(self) -> str:
        return f"Box contains {len(self.fruits)} fruit(s)"

    def add_fruit(self, fruit: Fruit) -> None:
        if self.volume + fruit.volume > self.capacity:
            raise BoxFullError(fruit)

        self.fruits.append(fruit)

    def __add__(self, other: object) -> Self:
        if not isinstance(other, Fruit):
            return NotImplemented

        self.add_fruit(other)
        return self

    def remove_fruit(self, fruit: Fruit) -> None:
        self.fruits.remove(fruit)

    def __sub__(self, other: object) -> Self:
        if not isinstance(other, Fruit):
            return NotImplemented

        self.remove_fruit(other)
        return self
