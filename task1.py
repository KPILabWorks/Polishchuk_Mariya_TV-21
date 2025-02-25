from itertools import zip_longest

def merge_strings(s1: str, s2: str) -> str:
    return ''.join(a + b if b else a for a, b in zip_longest(s1, s2, fillvalue=''))

def main():
    s1 = input("Введіть перший рядок: ")
    s2 = input("Введіть другий рядок: ")
    result = merge_strings(s1, s2)
    print("Результат:", result)

if __name__ == "__main__":
    main()
