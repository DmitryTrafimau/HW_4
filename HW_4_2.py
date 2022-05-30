import math
DATABASE = {
'gomi': {'corn grits': 100, 'water': 300, 'people': 3},
'samolina': {'semolina': 60, 'water': 150, 'milk': 150, 'people': 4},
'oatmeal': {'oat flakes': 60, 'water': 150, 'people': 1},
}
store = {
'corn grits': 3000, 'semolina': 1000, 'milk': 1500, 'oat flakes': 600, 'water': math.inf
}
def normalize_recipe(recipe, rp, dp):
    one_portion_recipe = {k: v/rp for k, v in recipe.items()}
    return {k: v * dp for k, v in one_portion_recipe.items()}
def check_availability(store, recipe):
    for k, v in recipe.items():
        if store[k] > recipe[k]:
            result = True
        else:
            result = False
        return result
def get_missed(store, recipe):
    result = {}
    for k, v in recipe.items():
        if store[k] < recipe[k]:
            result[k] = recipe[k] - store[k]
            int(result[k])
    return result

while True:
    name = input('what do you want?')
    choice = DATABASE.get(name)
    if choice == None:
        print('Нет такого рецепта')
    else:
        people = float(input('how many?'))
        normalized_choice = normalize_recipe(choice, choice.pop('people'), people)
        if check_availability(store, normalized_choice):
            print('your choice', name, 'needs', normalized_choice)
        else:
            print('you miss', get_missed(store, normalized_choice))
        if name == 'gomi':
            choice.update(people=3)
        elif name == 'samolina':
            choice.update(people=4)
        elif name == 'oatmeal':
            choice.update(people=1)