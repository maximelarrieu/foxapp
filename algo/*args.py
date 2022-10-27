def sum(*args):
    total = 0
    for number in args:
        total += number
    print(total)


def second_sum(*args):
    def real_sum(*numbers):
        total = 0
        for number in numbers:
            total += number
        return total

    print(real_sum(*args))


sum(2, 8, 7)
numbers = (10, 6, 14)
second_sum(*numbers)
