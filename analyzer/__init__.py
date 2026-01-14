"""
Pakiet analyzer - narzędzia do analizy danych liczbowych.

Eksportuje główne funkcje z modułów:
- read_numbers z io_utils
- mean, min_max z stats
- only_positive, only_even z filters
"""

from analyzer.io_utils import read_numbers
from analyzer.stats import mean, min_max
from analyzer.filters import only_positive, only_even

__all__ = [
    'read_numbers',
    'mean',
    'min_max',
    'only_positive',
    'only_even',
]
