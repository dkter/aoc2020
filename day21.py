from operator import or_
from functools import reduce

ingredient_map = {}
all_ingredients = set()
with open("day21.in") as f:
    for line in f:
        ingredients, allergens = line.strip(")\n").split(" (contains ")
        ingredients = frozenset(ingredients.split(" "))
        allergens = set(allergens.split(", "))
        all_ingredients |= ingredients

        ingredient_map[ingredients] = allergens

allergens = {}
for ingredient_set, allergen_set in ingredient_map.items():
    for allergen in allergen_set:
        if allergen not in allergens:
            allergens[allergen] = ingredient_set
        else:
            allergens[allergen] &= ingredient_set

used_ingredients = reduce(or_, allergens.values())

count = 0
for ingredient in all_ingredients:
    if ingredient not in used_ingredients:
        for ingredient_set in ingredient_map:
            if ingredient in ingredient_set:
                count += 1
print(count)

ingredients = {}
done = False
really_done = False
while not done:
    for allergen, ingredient_set in list(allergens.items()):
        done = True
        if len(ingredient_set) == 1:
            ingredients[next(iter(ingredient_set))] = allergen
        else:
            allergens[allergen] -= ingredients.keys()
            done = False

for allergen, ingredient_set in list(allergens.items()):
    ingredients[next(iter(ingredient_set))] = allergen
    
print(','.join(sorted(ingredients.keys(), key=lambda x: ingredients[x])))
