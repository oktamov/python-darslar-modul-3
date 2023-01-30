def iter_func():
    result = []
    for i in range(1, 21):
        if i % 2 == 0:
            result.append(f"-{i}")
        else:
            result.append(i)
    return result


iterator = iter(iter_func())


# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


def gen_func():
    for i in range(1, 21):
        if i % 2 == 0:
            yield f"-{i}"
        else:
            yield i


my_generator = gen_func()
print(next(my_generator))  # 1
print(next(my_generator))  # -2
print(next(my_generator))  # 3
print(next(my_generator))  # -4
