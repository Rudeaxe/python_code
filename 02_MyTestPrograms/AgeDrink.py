"""
Write a function 'problem1_5(age)'. This function should use if-elif-else
statement to print out
"Have a glass of milk." for anyone under 7;
"Have a coke." for anyone under 21,
"Have a martini." for anyone 21 or older

Tip: Be careful about the ages 7 (a seven year old is not under 7) and 21.
Also be careful to make the phrases exactly as shown for the auto-grader.
"""


def tell_my_drink(age):
    if age < 7:
        print("Drink Milk")
    elif age >= 7 and age < 21:
        print("Drink Coke")
    elif age >= 21 and age < 55:
        print("Drink Martini")
    elif age >= 55:
        print("Drink Numbu Pani")


age=int(input("Enter your age here: "))
tell_my_drink(age)




# print("Press 1 if your age is lessor than "7")
# print("Press 2 if your age is equal 7 lessor than 21")
# print("Press 3 if your age is equal to and  greater than 21")
# age= input("Enter your choice\n")
# if (age=='1'):
#     print("Have A Glass of Milk")
# elif(age=='2'):
#     print("Have A coke")
# elif(age=='3'):
#     print("Have A Martini")
