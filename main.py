#!/usr/bin/env python3
"""
Program testowy dla pakietu analyzer.
Wczytuje dane z pliku, filtruje je i oblicza statystyki.
"""

import sys

# Różne style importów zgodnie z wymaganiami
from analyzer import read_numbers, mean  # Import z __init__.py
from analyzer.filters import only_even   # Import bezpośredni z modułu
import analyzer.stats                     # Import całego modułu


def main():
    # Domyślna ścieżka do pliku z danymi
    file_path = 'data.txt'
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    
    try:
        # Wczytaj dane z pliku
        numbers = read_numbers(file_path)
        
        if not numbers:
            print("Plik nie zawiera żadnych liczb.")
            return
        
        # Filtruj: tylko dodatnie i parzyste
        # Używamy generatorów - najpierw filtrujemy dodatnie
        from analyzer.filters import only_positive
        positive_numbers = list(only_positive(numbers))
        
        # Następnie filtrujemy parzyste z dodatnich
        even_positive_numbers = list(only_even(positive_numbers))
        
        if not even_positive_numbers:
            print("Brak liczb dodatnich i parzystych w danych.")
            return
        
        # Oblicz statystyki używając różnych stylów importów
        avg = mean(even_positive_numbers)  # Używamy importu z __init__.py
        min_val, max_val = analyzer.stats.min_max(even_positive_numbers)  # Używamy importu modułu
        
        # Wypisz wyniki
        print(f"Mean: {avg}")
        print(f"Min, max: ({min_val}, {max_val})")
        
    except FileNotFoundError as e:
        print(f"Błąd: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Błąd danych: {e}", file=sys.stderr)
        sys.exit(1)
    except PermissionError as e:
        print(f"Błąd uprawnień: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
