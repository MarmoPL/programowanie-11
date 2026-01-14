#!/usr/bin/env python3

import sys

from analyzer import read_numbers, mean
from analyzer.filters import only_even
import analyzer.stats


def main():
    file_path = 'data.txt'
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    
    try:
        numbers = read_numbers(file_path)
        
        if not numbers:
            print("Plik nie zawiera żadnych liczb.")
            return
        
        from analyzer.filters import only_positive
        positive_numbers = list(only_positive(numbers))
        
        even_positive_numbers = list(only_even(positive_numbers))
        
        if not even_positive_numbers:
            print("Brak liczb dodatnich i parzystych w danych.")
            return
        
        avg = mean(even_positive_numbers)
        min_val, max_val = analyzer.stats.min_max(even_positive_numbers)
        
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
