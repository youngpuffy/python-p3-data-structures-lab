spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]
    
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level =  '🌶' * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None
    pass

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        heat_level = '🌶' * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
    pass

def get_average_heat_level(spicy_foods):
    total_heat =sum(food['heat_level'] for food in spicy_foods)
    return total_heat / len(spicy_foods) if spicy_foods else 0
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
