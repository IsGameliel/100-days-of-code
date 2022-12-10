# #write your code bellow this line
# def prime_checker(number):
#     for i in range(2, number):
#         if number % i == 0:
#             print("It's a prime number")
#         else:
#             print("It's not a prime number")
#         break

# #write your code above this line 

# # dont change the code below
# n = int(input("Check this number: "))
# prime_checker(number=n)


#write your code bellow this line
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("it's not a prime number")

#write your code above this line 

# dont change the code below
n = int(input("Check this number: "))
prime_checker(number=n)