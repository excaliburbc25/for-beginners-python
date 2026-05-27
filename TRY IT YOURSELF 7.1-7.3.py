#Activity 7.1 Rental Car
'''
Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”
'''
# car = input("What kind of car do you like?: ")
# if car == "Subaru":
#     print(f"We got your favorite {car}")
# else:
#     print("Sorry we dont have that kind of car.")
#Activity 7.2 Restaurant seating
'''
Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
'''
# restaurant = input("How many people are in their dinner group?: ")
# restaurant = int(restaurant)
# if restaurant <= 8:
#     print("Your table is ready!")
# else:
#     print("Sorry, you'll have to wait for a table for your group.")
#Activity 7.3 Multiples of Ten
'''
Ask the user for a number, and then report whether the number is a multiple of 10 or not.
'''
num = input("Type a number: ")
num = int(num)
if num % 10 == 0:
    print("The number is multiple of ten!")
else:
    print("The number is not multiple of ten!")