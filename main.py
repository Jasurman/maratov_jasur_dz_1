# def great_user():
# #     print('Hello Jasur!')
# # great_user()

# def great_user(username):
#     print(f"Hello {username.title()}!")
# great_user('jasur')

# def favorite_book(username, name_book):
#     print(f"One of my favorite books is {username.title()} in {name_book.title()} ")
# favorite_book('alice', 'wonderland')

# def descirbe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}")
#     print(f"My favorite {animal_type.title()}'s name is {pet_name.title()}")
# descirbe_pet('hamster', 'harry')
# descirbe_pet('dog', 'rokki')
# descirbe_pet(animal_type='cat', pet_name='mercik')

# def descirbe_pet(pet_name, animal_type='dog'):
#     print(f"\nI have a {animal_type}")
#     print(f"My favorite {animal_type.title()}'s name is {pet_name.title()}")
# descirbe_pet('rocki', 'hamster')
# descirbe_pet(animal_type='cat', pet_name='mercik')


# def make_shirt(name_str, num='l',):
#     print(f"\nРазмер футболки: {num.title()}\nТекс: {name_str.title()}")
# make_shirt('xl', 'i love python')
# make_shirt(num='l', name_str='omg')
# make_shirt('jasur maratov')
#
# def describe_city(city, country):
#     print(f"{city.title()} is in {country.title()}")
# describe_city('buxara', 'uzbekistan')
# describe_city('moscow', 'russia')
# describe_city('paris', 'france')

# def get_user(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# resualt = get_user('bekzod', 'yuldashev', 'beka')
# print(resualt)
# resualt = get_user('jasur', 'maratov')
# print(resualt)

# def build_person(first_name, last_name, age=None):
#     person = {'first': first_name.title(), 'last': last_name.title()}
#     if age:
#         person['age']= age
#     return person
#
# resualt = build_person('maratov', 'jasur')
# print(resualt)
# resualt = build_person('maratov', 'jasur', 28)
# print(resualt)

def get_user(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("First name: ")
    if l_name == 'q':
        break


    resualt = get_user(f_name, l_name)
    print(f"Hello, {resualt}!")
