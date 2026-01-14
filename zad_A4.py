#!/usr/bin/env python3
"""
Zadanie A4: Mini-system plików (Pathlib + Dataclass + JSON)
Przechodzi rekurencyjnie po katalogu i zapisuje informacje o plikach do JSON.
"""

import sys
import json
from pathlib import Path
from dataclasses import dataclass, asdict


@dataclass
class FileInfo:
    """Reprezentacja informacji o pliku."""
    path: str
    size: int
    suffix: str


def scan_directory(base_path: Path) -> list[FileInfo]:
    """
    Rekurencyjnie przechodzi po katalogu i zbiera informacje o plikach.
    """
    files = []
    
    try:
        for item in base_path.rglob('*'):
            if item.is_file():
                try:
                    relative_path = item.relative_to(base_path)
                    size = item.stat().st_size
                    suffix = item.suffix
                    
                    file_info = FileInfo(
                        path=str(relative_path),
                        size=size,
                        suffix=suffix
                    )
                    files.append(file_info)
                except PermissionError:
                    print(f"Ostrzeżenie: Brak uprawnień do odczytu '{item}'", file=sys.stderr)
                except OSError as e:
                    print(f"Ostrzeżenie: Nie można odczytać '{item}': {e}", file=sys.stderr)
    except PermissionError:
        print(f"Błąd: Brak uprawnień do przeszukania katalogu '{base_path}'", file=sys.stderr)
        sys.exit(1)
    
    return files


def main():
    if len(sys.argv) < 3:
        print("Użycie: python zad_A4.py <katalog> <plik_wyjściowy.json>", file=sys.stderr)
        sys.exit(1)
    
    directory = sys.argv[1]
    output_file = sys.argv[2]
    
    base_path = Path(directory)
    
    # Sprawdź czy katalog istnieje
    if not base_path.exists():
        print(f"Błąd: Katalog '{directory}' nie istnieje.", file=sys.stderr)
        sys.exit(1)
    
    if not base_path.is_dir():
        print(f"Błąd: '{directory}' nie jest katalogiem.", file=sys.stderr)
        sys.exit(1)
    
    # Skanuj katalog
    files = scan_directory(base_path)
    
    # Konwertuj do listy słowników
    files_data = [asdict(f) for f in files]
    
    # Zapisz do JSON
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(files_data, f, indent=2, ensure_ascii=False)
    except PermissionError:
        print(f"Błąd: Brak uprawnień do zapisu pliku '{output_file}'.", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Błąd wejścia/wyjścia: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
