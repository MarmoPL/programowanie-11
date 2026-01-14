from typing import Iterator, Iterable


def only_positive(data: Iterable[float]) -> Iterator[float]:
    for value in data:
        if value > 0:
            yield value


def only_even(data: Iterable[float]) -> Iterator[float]:
    for value in data:
        if value % 2 == 0:
            yield value
