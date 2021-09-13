# Intro to Python
# Differences:
# snake_case rather than camelCase
# No semicolons ; no curly braces {}, instead use
# indentation and whitespace
# print() instead of console.log()

# Declare a variable and print it to the console
my_cool_variable = "I love python!"
print(my_cool_variable)

# Ask the user for input
# favorite_number = input("What's your favorite number?\n")
# print("Your favorite number is", favorite_number)

############################
# Common Data Types:
my_string = "Tis but a flesh wound!" # str type
my_int = 42 # int type
my_float = 0.12345 # float type
no_data = None # None type, like null or undefined
# We need to learn about: arrays, objects, boolean

is_weather_good = True # booleans!
is_cold_outside = False

# Tuple type - immutable set of data
my_coordinates = (50, 75, (100, 200))
print(my_coordinates)
print("Your X coordinate is:", my_coordinates[0])
print("Your Y coordinate is:", my_coordinates[1])
print("Your Z coordinate is:", my_coordinates[2])

# Type Checking
print(my_string, type(my_string))
print(my_int, type(my_int))
print(my_float, type(my_float))
print(no_data, type(no_data))
print(is_weather_good, type(is_weather_good))

# Type Conversion
some_num = '43'
my_int = int(some_num) # Type conversion or "casting"
print(type(my_int))



# Lists (are like array from JS)

# String Interpolation 2 ways!
phrase_1 = "That's the way"
phrase_2 = "aha aha"
phrase_3 = "I like it"

# 1st method: .format()
# let chorus = `${phrase_1}`
chorus = "{}, {}, {}!, {}".format(phrase_1, phrase_2, phrase_3, phrase_2)
print(chorus)

# 2nd method: f-string
chorus = f"{phrase_1}, {phrase_2}, {phrase_3}!, {phrase_2}"
print(chorus)

# Dictionaries (are like objects from JS)

knight = {
    'name': 'Arthur',
    'has_table': True,
    'title': 'King of England',
    'likes': ['chivalry', 'the holy grail']
}

# Multi-line string """asdf"""
greeting = f"""
Greetings! I am {knight['name']}, {knight['title']}.
    I thoroughly enjoy {knight['likes']}
"""
print(greeting)


###########################
# Numerical operations
# What is the resulting data type going to be??
print(15 / 5) # 3.0 float type
print(int(15 / 5)) # 3 int type
print(14 // 5) # 2 forced integer division
print(2 ** 3) # 2 to the power of 3
print(7 % 3) # 1

###########################
# Logical operators and Control flow
# instead of && its and
# instead of || its or
# instead of ! its not

is_sunday = False
is_monday = True
is_sunny = False

# If it's sunday, I'm ordering Chicken wings
# If it's monday and it's not sunny im ordering some pizza
# Otherwise i'm cooking at home

# 💪 Exercise: Convert the above text into a if elif else statement
if is_sunday:
    print('Ordering Chicken Wings!')
elif is_monday and not is_sunny:
    print('Ordering some Pizza!')
else:
    print('Cooking at home!')

########################
# Loops

# while loops
count = 0
while count < 5:
    print(count, "is less than 5")
    count = count + 1
else:
    print(count, "is finally 5")

# for loops
# for loop that counts from 0 to 4
for i in range(5):
    print(i)

# for loop that counts the odd numbers from 11 and 17
for i in range(11, 19, 2):
    print(i)

###################
# Functions
def add(num_one, num_two):
    """Returns the sum of the two input numbers"""
    return num_one + num_two

num_1 = 9
num_2 = 100
print(f'The result of {num_1} + {num_2}  = ', add(num_1, num_2))

####################
# Lists
secret_files = ['a', 'b', 'c']
more_secret_files = ['d', 'e', 'f']

print(secret_files + more_secret_files)
print(len(secret_files + more_secret_files))

secret_files.append('z')
print(secret_files)

secret_files.extend(more_secret_files)
print(secret_files)

##############
# Dictionary Methods

knight = {
    'name': 'Arthur',
    'has_table': True,
    'title': 'King of England',
    'likes': ['chivalry', 'the holy grail']
}

# Access a key:value pair
print(knight['name'])

# Set a key:value pair
knight['num_castles'] = 2

# Delete a key:value pair
del knight['has_table']
print(knight)

# How to iterate over all the key:value pairs of an 
# dictionary
# .items()
print(knight.items())

for key, val in knight.items():
    print(f'{key} : {val}')