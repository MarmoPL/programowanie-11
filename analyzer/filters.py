"""
Moduł filters - funkcje filtrujące dla pakietu analyzer.
"""

from typing import Iterator, Iterable


def only_positive(data: Iterable[float]) -> Iterator[float]:
    """
    Filtruje dane, zwracając tylko liczby dodatnie.
    
    Args:
        data: Iterable z liczbami.
        
    Yields:
        Liczby większe od 0.
    """
    for value in data:
        if value > 0:
            yield value


def only_even(data: Iterable[float]) -> Iterator[float]:
    """
    Filtruje dane, zwracając tylko liczby parzyste.
    
    Args:
        data: Iterable z liczbami.
        
    Yields:
        Liczby parzyste (podzielne przez 2).
    """
    for value in data:
        if value % 2 == 0:
            yield value
