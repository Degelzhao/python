def make_sandwich(*formulas):
    for formula in formulas:
        print('this is ' + formula + ' sandwich')

make_sandwich('met', 'beef', 'mutton')

def build_profile(first_name, last_name, **user_inf):
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name

    for key, value in user_inf.items():
        profile[key] = value

    return profile

user_profile = build_profile('Zhao', 'Wei', age = 25, hobby = 'Dota2')
print(user_profile)


def make_car(manufacturers, model, **car_inf):
    inf = {}
    inf['manufacturers'] = manufacturers
    inf['model'] = model

    for key, value in car_inf.items():
        inf[key] = value
    return inf

car = make_car('Porsche', 911, color = 'yellow', parts = 'turbo')
print(car)