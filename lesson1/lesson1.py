#1. Create variables john_salary and marta_salary of some type (floating point).
# Assign the created variables the values you want.
# Print the values of both variables to the console using the print method

john_salary = 10.5
marta_salary = 8.3
print('john_salary: ', john_salary)
print('marta_salary: ', marta_salary)

#2. Create variables john_age and marta_age of integer type.
# Assign the created variables the values you want.
# Print the values of both variables to the console using the print method.

john_age = 28
marta_age = 26
print('john_age: ', john_age)
print('marta_age: ', marta_age)

#3. Create string type variables john_name and marta_name.
# Assign the created variables the values you want.
# Print the values of both variables to the console using the print method.

john_name = 'Johny'
marta_name = 'Mary'
print('john_name: ', john_name)
print('marta_name: ', marta_name)

#4. Create boolean variables john_gender and marta_gender.
# Let john be false and Marta be true.
# Print the values of both variables to the console using the print method.

john_gender = False
marta_gender = True
print('john_name: ', john_name)
print('marta_name: ', marta_name)

#5. Create variables john_friends and marta_friends.
# Assign lists to variables. Each list must contain the names of friends.
# John has his list of friends and Martha has hers.
# Friends (friend's name) can be the usual strings "James", "Peter", etc.

john_friends = ['Andrew', 'David', 'Jack']
marta_friends = ['Lynda', 'Katty', 'Bob']
print('john_friends: ', john_friends)
print('marta_friends: ', marta_friends)

#6. Create a list with people's names, some names should be repeated in it.
# Turn a list of duplicate names into a list of unique names using sets.

people_list = ['Volod', 'Taras', 'Artem', 'Max', 'Taras', 'Artem', 'Frank']
people_set = set(people_list)
print(people_set)

#7. Create 2 tuple variables.
#The tuple must consist of 2 floating point numbers.
# The first value of the tuple is the latitude where you live,
# and the second value is the longitude where you live.

coordinate_john = (50.611265, 26.2474565)
coordinate_marta = (50.5991, 26.2474565)
print('coordinate_john: ', coordinate_john)
print('coordinate_marta: ', coordinate_marta)

#8. Create 2 variables john, marta.
# Variables must be dictionaries with keys:
# full_name, age, salary, gender, friends, coordinates.

john = {
    'full_name' : john_name,
    'age' : john_age,
    'salary' : john_salary,
    'gender' : john_gender,
    'friends' : john_friends,
    'coordinates' : coordinate_john
        }
marta = {
    'full_name' : marta_name,
    'age' : marta_age,
    'salary' : marta_salary,
    'gender' : marta_gender,
    'friends' : marta_friends,
    'coordinates' : coordinate_marta
         }
for key, value in john.items():
   print(key, '=>', value)
for key, value in marta.items():
    print(key, '=>', value)