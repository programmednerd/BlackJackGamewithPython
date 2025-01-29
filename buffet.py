restaurant_menu = ('pizza', 'pasta', 'toasties', 'salads', 'desserts')
for food in restaurant_menu:
    print(f"We currently offer {food.title()}.")

restaurant_menu = ('pizza', 'pasta', 'french fries', 'cakes', 'coffie')
for food in restaurant_menu:
    print(f"New restaurant offer: {food.title()}.")


print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for food in restaurant_menu:
    print(f"{food.title()}")



pizzas = ['margarita', '4 cheese', 'prosciutto', 'creamy']
for pizza in pizzas:
    if pizza == '4 cheese':
        print(pizza.upper())
    else: 
        print(pizza.title())

pizza = 'margarita'
print("Is pizza == 'prosciutto'? I predict True")
print(pizza == 'prosciutto')

print("\nIs pizza == 'margarita' I predict True")
print(pizza == 'margarita')



age = 16

if age == 18:
    print("You're legal to drink")
else:
    print("You need permission from your parents!")

fav_number = 90

if fav_number != 13:
    print("You're wrong! Try again later.")
else:
    print("You're right!!")

fav_number = 90

if fav_number != 13:
    print
