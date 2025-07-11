# Events that effects the execution of a program


# try:
#     a = 10
#     b = 0
#     print(a/b)

# except:
#     print("you have an error")

# print('Alwin')

# try:
#     a = 5
#     b = 0
#     print(a/b)

# except Exception as e:
#     print("you have an error",e)
# print("Alwin")

# Multiple exception handling

# try:
#     a = int(input("enter your number:"))
#     b = int(input("enter your number:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("you cannot divide a number with zero")
# except ValueError:
#     print("invalid data for type")
# except TypeError:
#     print("check your data")
# finally:
#     print("this will always execute")
# print("Alwin")

#Raise Keyword

# a = int(input("enter number"))
# if a > 10:
#     raise ValueError (a,'should be lower')

# class MyError(Exception):
#     pass
# a = int(input("enter a number: "))
# if a < 10:
#     raise MyError(a,'should be greter than 20')

# List Comprehension

# Normal Method

# a = []
# for i in range(1,100):
#     a.append(i)
# print(a)

# Comprehension Method

# sqr = [i**2 for i in range(1,100)]
# print(sqr)

# even = [i for i in range(1,100) if i%2 == 0]
# print(even)



# ---------------class in work--------------------

# first 100 numbers, print numbers divisible by 7 and 3

# result = [i for i in range(1,1000) if i%3 == 0 and i%7 == 0] 
# print(result)

# result = [i for i in range(1,1000) if '6'in str(i)]
# print(result)

