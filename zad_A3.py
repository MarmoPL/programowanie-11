#!/usr/bin/env python3
"""
Zadanie A3: Generowanie i filtrowanie danych + JSON
Generuje liczby podzielne przez 3 i 4, zapisuje N pierwszych do pliku JSON.
"""

import json
import itertools


def divisible_by_3_and_4():
    """
    Generator nieskończony zwracający liczby podzielne przez 3 i 4 (czyli przez 12).
    Uwaga: zgodnie z przykładem w zadaniu [0, 15, 30, 45, 60] - to są liczby podzielne
    przez 15, nie przez 12. Implementuję zgodnie z przykładem (podzielne przez 3 I 4
    rozumiane jako podzielne przez 3 LUB podzielne przez 4, ale nie tylko przez jedno).
    
    Po analizie przykładu: 0, 15, 30, 45, 60 - to wielokrotności 15.
    Warunek "podzielne przez 3 i 4" może oznaczać podzielne przez NWW(3,4)=12
    lub może być błąd w przykładzie.
    
    Implementuję zgodnie z przykładem - wielokrotności 15 (podzielne przez 3 AND 5?).
    Ale to nie ma sensu z treścią zadania.
    
    Zakładam że przykład zawiera błąd i implementuję zgodnie z treścią:
    liczby podzielne przez 3 I przez 4 (czyli przez 12): 0, 12, 24, 36, 48...
    """
    for n in itertools.count(0):
        if n % 3 == 0 and n % 4 == 0:
            yield n


def main():
    try:
        n = int(input())
    except ValueError:
        print("Błąd: Podaj poprawną liczbę całkowitą.")
        return
    except EOFError:
        print("Błąd: Brak danych wejściowych.")
        return
    
    if n < 0:
        print("Błąd: N musi być nieujemne.")
        return
    
    # Pobierz pierwsze N liczb z generatora
    generator = divisible_by_3_and_4()
    numbers = list(itertools.islice(generator, n))
    
    # Zapisz do pliku JSON
    try:
        with open('out.json', 'w', encoding='utf-8') as f:
            json.dump(numbers, f)
    except PermissionError:
        print("Błąd: Brak uprawnień do zapisu pliku 'out.json'.")
        return
    except IOError as e:
        print(f"Błąd wejścia/wyjścia: {e}")
        return


if __name__ == "__main__":
    main()
