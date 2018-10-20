#using python write a program to find prime numbers 0 to 100

number = int(input("Enter the number to check Prime Number"))
#########################################################################

isPrime = 1
for i in range (2,number):
    remainder = number %i
    if(remainder == 0):
        isPrime = 0
        break;
if (isPrime == 0):
    print ("Number is Not Prime")
else:
    print ("Number is Prime" )


###########################################################################
# isPrime = 1 # initialize flag as "number is a prime number"
# for loop_number in range(2, number):
#     remainder = number % loop_number
#     if(remainder == 0):  # the number is completly divisible, hence not a prime number
#         isPrime = 0
#         break;
#
# if(isPrime == 0):
#     print ("Number is not prime")
# else:
#     print("Number is prime")


########################################################
