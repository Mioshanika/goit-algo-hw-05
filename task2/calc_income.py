from typing import Callable, Generator
from re import findall

def generator_numbers(text: str) -> Generator[float]:
    pattern = r'\s\d+\.\d+\s'
    found_patterns = findall(pattern, text)
    for num in found_patterns:
        yield float(num)
     
def sum_profit(text: str, func: Callable) -> float:
    sum = 0.00
    for num in func(text):
        sum += num
    return sum

def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як \
        основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

if __name__ == '__main__':
    main()