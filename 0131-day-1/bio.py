'''
Take in as user input
biographical info and
print out succinctly
'''

name = input("Enter name: ")
birth_year = int(input("Enter birth year: "))
hobby = input("Enter hobby: ")
food = input("Enter food: ")

# print info
print(f"Hello, your name is {name}, you were born in {birth_year}, " +
      f"your favorite hobby is {hobby}, your favorite food is {food}.")
# calculate and print age as of 2026
age = 2026 - birth_year
print(f"As of 2026, you are roughly {age} years old.")