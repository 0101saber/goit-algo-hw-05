from typing import Callable
import re


def generator_numbers(text: str):
    for number in re.findall(r'\b\d+.\d+\b', text):
        yield float(number)


def sum_profit(text: str, funk: Callable):
    total_income = 0
    for num in funk(text):
        total_income += num

    return total_income
