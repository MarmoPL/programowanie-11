import json
import itertools

def divisible_by_3_and_4():
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
    
    generator = divisible_by_3_and_4()
    numbers = list(itertools.islice(generator, n))
    
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
