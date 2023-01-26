"""vazifa 1"""


def get_next_multiple(num):
    while True:
        yield num
        num += 5


a = 5
two = get_next_multiple(a)
# print(next(two))
# print(next(two))
# print(next(two))
# print(next(two))

"""vazifa 2"""


def get_next_prime():
    num = 2
    while True:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num
        num += 1


prime_generator = get_next_prime()
# print(next(prime_generator))  # 2
# print(next(prime_generator))  # 3
# print(next(prime_generator))  # 5

"""vazifa 3"""


def add(a, b):
    def get_add():
        return (a + b) * 2
    return get_add()


# print(add(2,3)) # 10



"""vazifa 4"""


def only_even_parametrs(func):
    def even_inner(*args):

        for arg in args:
            if arg % 2 == 0:
                return func(*args)
            else:
                return "Please add only even numbers!"

    return even_inner


@only_even_parametrs
def add(a, b):
    return a + b


# print(add(2, 4))  # 6
# print(add(3, 4))  # faqat juft sonlar kiritilsin!



"""vazifa 5"""


def decarator(func):
    def list_index(list_):
        count = 0
        if type(list_) == list:
            for index, val in enumerate(list_):
                count += index
        else:
            return "Please send only list"
        return func(count)

    return list_index


@decarator
def sum_index(lists):
    return lists


print(sum_index([1, 2, 3, 4]))  # 6
print(sum_index((1, 2, 3, 4)))  # Please send only list
