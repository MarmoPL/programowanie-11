"""
Moduł stats - funkcje statystyczne dla pakietu analyzer.
"""

from typing import Iterable


def mean(data: Iterable[float]) -> float:
    """
    Oblicza średnią arytmetyczną.
    
    Args:
        data: Iterable z liczbami.
        
    Returns:
        Średnia arytmetyczna.
        
    Raises:
        ValueError: Gdy dane są puste.
    """
    data_list = list(data)
    
    if not data_list:
        raise ValueError("Nie można obliczyć średniej z pustych danych.")
    
    return sum(data_list) / len(data_list)


def min_max(data: Iterable[float]) -> tuple[float, float]:
    """
    Znajduje wartość minimalną i maksymalną.
    
    Args:
        data: Iterable z liczbami.
        
    Returns:
        Krotka (min, max).
        
    Raises:
        ValueError: Gdy dane są puste.
    """
    data_list = list(data)
    
    if not data_list:
        raise ValueError("Nie można obliczyć min/max z pustych danych.")
    
    return (min(data_list), max(data_list))
