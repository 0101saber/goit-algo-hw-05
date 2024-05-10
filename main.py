from task1 import caching_fibonacci
from task2 import generator_numbers, sum_profit

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # first task
    fib = caching_fibonacci()
    print('First task')
    print(fib(10))
    print(fib(15))
    print(20 * '#')

    # second task
    print('Second task')
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
    print(20 * '#')