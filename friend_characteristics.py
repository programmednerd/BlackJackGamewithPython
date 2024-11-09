friend_characteristics = {'first name': 'Elitsa', 'last name': 'Stoynova', 'age': 23, 'city': 'Amsterdam'}
for key, value in friend_characteristics.items():
    print(f"Her {key} is {value}.")

new_numbers = {'Elitsa': 13, 'Sam': 23, 'Bouke': 50, 'Boryana': 7}
for name, number in new_numbers.items():
    print(f"{name.title()}'s favourite number is {number}.")


new_definitions = {'key-value pairs': 'each key is connected to a value, and you can use a key to access the value associated with that key.', 'del': 
                   'removes a key/value pair'}
for term, definition in new_definitions.items():
    if term == 'key-value pairs':
        print(f"\n{term.title()} mean that {definition}")
    if term == 'del':
        print(f"\nA {term.title()} statement means that it {definition} from the dictionary.")



rivers = {'nile': 'egypt', 'maritsa': 'bulgaria', 'donau': 'germany', 'maas': 'netherlands'}
for river, country in rivers.items():
    print(f"{river.title()} river is located in {country.title()}.")


favourite_languages = {'elitsa': 'python', 'sammy': 'css', 'bouke': 'c', 'boryana': 'react', 'maxi': 'N/A'}
for name, language in favourite_languages.items():
    if name == 'maxi':
        print('Please take the poll!')
    if name != 'maxi':
        print('Thank you for taking the poll!')



favourite_languages2 = {'jen': ['python', 'rust'],
                        'sarah': ['c'],
                        'edward': ['rust', 'go'],
                        'phil': ['python', 'haskell'],    
}

for name, languages in favourite_languages2.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")


users = {
    'elbstynv': {
        'first': 'elitsa',
        'last': 'stoynova',
        'location': 'amsterdam',
        },
    'bkingma': {
        'first': 'bouke',
        'last': 'kingma',
        'location': 'maastricht',
        },

}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


friend_0 = {'first_name': 'polya', 
            'last_name': 'baturova', 
            'age': 24, 
            'location': 'amsterdam', 
}

friend_1 = {'first_name': 'boryana',
            'last_name': 'stoynova',
            'age': 16,
            'location': 'hueckelhoven'
}

people = [friend_0, friend_1]

for friend in people:
    print(friend)



pet_0 = {'animal': 'cat', 'name': 'maxi', 'owner': 'sammy'}
pet_1 = {'animal': 'cat', 'name': 'leo', 'owner': 'sidney'}

pets = [pet_0, pet_1]

for pet in pets:
    print(pet)