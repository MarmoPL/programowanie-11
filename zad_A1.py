#!/usr/bin/env python3
"""
Zadanie A1: Analiza logów tekstowych
Analizuje logi zapisane w pliku tekstowym i wypisuje 3 najczęściej występujące słowa.
"""

import sys
from collections import Counter


def analyze_logs(file_path: str) -> Counter:
    """
    Wczytuje plik z logami i liczy częstość występowania słów.
    Pomija puste linie i linie zaczynające się od #.
    Słowa są traktowane nieczule na wielkość liter.
    """
    word_counter = Counter()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # Pomijamy puste linie i komentarze
                if not line or line.startswith('#'):
                    continue
                # Dzielimy linię na słowa i liczymy (lowercase)
                words = line.lower().split()
                word_counter.update(words)
    except FileNotFoundError:
        print(f"Błąd: Plik '{file_path}' nie istnieje.", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Błąd: Brak uprawnień do odczytu pliku '{file_path}'.", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Błąd wejścia/wyjścia: {e}", file=sys.stderr)
        sys.exit(1)
    
    return word_counter


def main():
    if len(sys.argv) < 2:
        print("Użycie: python zad_A1.py <ścieżka_do_pliku>", file=sys.stderr)
        sys.exit(1)
    
    file_path = sys.argv[1]
    word_counter = analyze_logs(file_path)
    
    # Wypisujemy 3 najczęściej występujące słowa
    for word, count in word_counter.most_common(3):
        print(f"{word} {count}")


if __name__ == "__main__":
    main()
