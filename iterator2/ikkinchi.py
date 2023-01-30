def gen_func():
    try:
        with open('test.txt', 'r') as f:
            text = f.read()
        for char in text:
            yield char
    except FileNotFoundError as e:
        print(e)


my_generator = gen_func()
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
