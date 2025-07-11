# def bmi()
#     bmi = weight / (height **2)
# if bmi < 18.5:
#     status = 'underweight'
#     if bmi < 24.9:
#         status = 'normal weight'





#passing multiple arguments to function

# def addz(*args): #recieves as a tuple
#     s = 0
#     for i in args:
#         s += 1
#         return s
    
#  print(addz(2,3,5,2,3,1,3,4,9,2,1,32,2,2,1,1,2,3,4,4,6,7,9,0))


# def fulname(*args,**kwargs):
#     print(args)
#     print(kwargs)

# def fullname (**kwargs):
#     f = ''
#     for i in kwargs:
#         f = f+ kwargs[i]+' '
#     return f


# # printfullname(fname = 'robert',mname = 'downie', lname = 'jr'))
# print(2,3,5,2,3,1,3,4,9,2,1,32,2,2,1,1,2,3,4,4,6,7,9,0)
# print()

# p = lambd a x,y,z : x+y+z
# print(p(1,2,3))

# sqr = lambda x:x**2
# print(sqr(6))

#multiple of 3 numbers

# sumz = lambda a,b,c,d,e : a+b+c+d+e
# z = (sumz(1,2,3,4,5))
# print(z,z/5)

# sqrt = lambda n : n**0.5
# print(sqrt(25))

# peri = lambda r: 2*3.14*r
# print(peri(10))

#eligible if age>= 18 else 'not eligible'

# check = lambda age : true if age>= 18 else False
# print(check(11))


#scope of a variable
#recursion

# def hello():
#     print('hello guys')
#     return hello()

# hello()

# def counttozero (n):
#     print(n)
#     if n == 0:
#         return 0
#     return counttozero (n-1)

# counttozero (10)

#sum of first 10 numbers

# def counttozero (n):
#     if n == 10:
#         return 0
#     return 5+counttozero(n+1)

# print(counttozero(0))