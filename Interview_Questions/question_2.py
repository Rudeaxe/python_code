#Using python write a Program to find a given number is odd or even.
def get_input():
    user_input = int (input("Enter the number to check whether number is odd or even: "))
    return user_input

def get_input_range():
    user_input_inital = int (input("Enter the inital number to check whether number is odd or even: "))
    user_input_final = int (input("Enter the final number to check whether number is odd or even: "))

    #return {user_input_inital , user_input_final}
    return {"initial" : user_input_inital , "final" : user_input_final}

def cal_odd_even_range(hit_inital , hit_final):
    for i in range (hit_inital,hit_final+1):
        result = cal_odd_even(i)
        print(i, ":",result)


def cal_odd_even(number_to_check):
    if(number_to_check == 0 ):
        return "Number is zero. "
    else:
        remainder = number_to_check % 2
        if (remainder == 0):
            return "Given Number is Even."
        else:
            return "Given Number is Odd"


def main():
    #returned_val = get_input()
    returned_val_set  = get_input_range()
    #result = cal_odd_even(returned_val_set[0], returned_val_set[1])
    result = cal_odd_even_range(returned_val_set.get('initial'), returned_val_set.get('final'))
    #print (result )

# for i in range (1,User_Number):
#     remainder = User_Number %2
#     if (remainder == 0) :
#         print("Given Number is Even.")
#     else:
#         print("Given Number is Odd")
#

if __name__ == "__main__":
    main()