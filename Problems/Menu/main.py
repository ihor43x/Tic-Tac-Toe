menu = {"pizza": "Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy",
        "salad": "Caesar salad, Green salad, Tuna salad, Fruit salad",
        "soup": "Chicken soup, Ramen, Tomato soup, Mushroom cream soup"}
try:
    print(menu[input()])
except KeyError:
    print("Sorry, we don't have it in the menu")
