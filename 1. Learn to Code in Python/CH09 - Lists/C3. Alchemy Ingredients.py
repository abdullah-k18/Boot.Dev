def check_ingredient_match(recipe, ingredients):
    correct = 0
    incorrect_ingredients = []

    for ingredient in recipe:
        if ingredient in ingredients:
            correct += 1
        else:
            incorrect_ingredients.append(ingredient)

    percentage = correct / len(recipe) * 100
    return percentage, incorrect_ingredients

