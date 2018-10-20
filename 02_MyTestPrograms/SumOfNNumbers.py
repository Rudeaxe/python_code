
"""
#Write a function problem1_3(n) that adds up the numbers 1 through n and
#prints out the result. You should use either a 'while' loop or a 'for' loop.
#Be sure that you check your answer on several numbers n.  Be careful that your
#loop steps through all the numbers from 1 through and including n.
"""

n=input("Enter the number you want to calculate\n")

sum = 0
if n.isdigit():
    n = int(n)
    for i in range(n+1):
        sum = sum + i
    print("Sum =", sum)
print("Plz enter only digits...Try again")
