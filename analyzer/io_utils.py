from typing import Iterator


def read_numbers(path: str) -> list[float]:
    numbers = []
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                
                if not line:
                    continue
                
                try:
                    number = float(line)
                    numbers.append(number)
                except ValueError:
                    raise ValueError(
                        f"Niepoprawna wartość w linii {line_num}: '{line}'"
                    )
    except FileNotFoundError:
        raise FileNotFoundError(f"Plik '{path}' nie istnieje.")
    except PermissionError:
        raise PermissionError(f"Brak uprawnień do odczytu pliku '{path}'.")
    
    return numbers
