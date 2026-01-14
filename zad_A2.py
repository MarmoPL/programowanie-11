#!/usr/bin/env python3
"""
Zadanie A2: Przetwarzanie danych liczbowych w CSV
Wczytuje plik CSV, oblicza statystyki dla kolumn numerycznych i zapisuje wynik.
"""

import sys
import csv
import math
from statistics import mean, median


def is_numeric(value: str) -> bool:
    """Sprawdza czy wartość jest numeryczna."""
    if not value or not value.strip():
        return False
    try:
        float(value.strip())
        return True
    except (ValueError, TypeError):
        return False


def calculate_stdev(values: list) -> float:
    """Oblicza odchylenie standardowe próbki (dzielenie przez n-1)."""
    if len(values) < 2:
        return 0.0
    avg = mean(values)
    variance = sum((x - avg) ** 2 for x in values) / (len(values) - 1)
    return math.sqrt(variance)


def process_csv(input_path: str, output_path: str):
    """Przetwarza plik CSV i oblicza statystyki."""
    try:
        with open(input_path, 'r', encoding='utf-8', newline='') as f:
            reader = csv.reader(f)
            
            # Wczytaj nagłówek
            try:
                header = next(reader)
            except StopIteration:
                print("Błąd: Plik CSV jest pusty.", file=sys.stderr)
                sys.exit(1)
            
            # Wczytaj wszystkie wiersze
            rows = list(reader)
    
    except FileNotFoundError:
        print(f"Błąd: Plik '{input_path}' nie istnieje.", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Błąd: Brak uprawnień do odczytu pliku '{input_path}'.", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Błąd wejścia/wyjścia: {e}", file=sys.stderr)
        sys.exit(1)
    
    num_cols = len(header)
    
    # Najpierw określ które kolumny są numeryczne
    # Kolumna jest nienumeryczna jeśli zawiera co najmniej jedną wartość nienumeryczną
    # (puste wartości nie liczą się jako nienumeryczne)
    column_has_non_numeric = {i: False for i in range(num_cols)}
    
    for row in rows:
        if not row or all(cell.strip() == '' for cell in row):
            continue
        for i in range(num_cols):
            cell = row[i].strip() if i < len(row) else ''
            if cell:  # Niepuste pole
                if not is_numeric(cell):
                    column_has_non_numeric[i] = True
    
    # Kolumny numeryczne to te, które nie mają żadnej wartości nienumerycznej
    numeric_column_indices = [i for i in range(num_cols) if not column_has_non_numeric[i]]
    
    # Zbierz wiersze, które mają kompletne dane dla wszystkich kolumn numerycznych
    complete_rows = []
    for row in rows:
        if not row or all(cell.strip() == '' for cell in row):
            continue
        
        # Sprawdź czy wiersz ma wartości dla wszystkich kolumn numerycznych
        is_complete = True
        for i in numeric_column_indices:
            cell = row[i].strip() if i < len(row) else ''
            if not cell or not is_numeric(cell):
                is_complete = False
                break
        
        if is_complete:
            complete_rows.append(row)
    
    # Oblicz statystyki dla każdej kolumny numerycznej
    column_means = {}
    for i in numeric_column_indices:
        values = [float(row[i].strip()) for row in complete_rows]
        if values:
            col_mean = mean(values)
            col_median = median(values)
            col_std = calculate_stdev(values)
            column_means[i] = col_mean
            print(f"Column '{header[i]}': mean={col_mean}, median={col_median}, std={col_std}")
    
    # Zapisz nowy plik CSV
    try:
        with open(output_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            
            # Nagłówek z dodatkowymi kolumnami _dev
            new_header = header.copy()
            for i in numeric_column_indices:
                new_header.append(f"{header[i]}_dev")
            writer.writerow(new_header)
            
            # Zapisz tylko kompletne wiersze z odchyleniami
            for row in complete_rows:
                new_row = list(row[:num_cols])
                for i in numeric_column_indices:
                    cell = row[i].strip()
                    deviation = float(cell) - column_means[i]
                    new_row.append(deviation)
                writer.writerow(new_row)
    
    except PermissionError:
        print(f"Błąd: Brak uprawnień do zapisu pliku '{output_path}'.", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Błąd wejścia/wyjścia: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    if len(sys.argv) < 3:
        print("Użycie: python zad_A2.py <plik_wejściowy.csv> <plik_wyjściowy.csv>", file=sys.stderr)
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    process_csv(input_path, output_path)


if __name__ == "__main__":
    main()
