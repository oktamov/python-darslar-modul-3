def gen_func():
    try:
        with open('planets.txt', 'r') as f:
            text = f.readlines()
            for char in text:
                if "name" in char:
                    yield char.split("=")[1]
    except FileNotFoundError as e:
        print(e)


planets_gen = gen_func()
print(next(planets_gen))  # Mercury
print(next(planets_gen))  # Venus
print(next(planets_gen))  # Earth
print(next(planets_gen))  # Mars
