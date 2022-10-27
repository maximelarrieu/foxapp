names = ['Bob', 'Alice', 'John']


def say_hello(names):
    total = 0
    names[0] = "Bobette"
    for name in names:
        print('Hello', name)
        total += 1
    return total


def say_greeting(names, greeting="Hi"):
    for name in names:
        print(greeting + ' ' + name)


count = say_hello(names)
print("Said hello {} times".format(count))
print(names)
say_greeting(names)
