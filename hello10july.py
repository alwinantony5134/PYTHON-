# def find_missing_number(arr):
#     n = len(arr) + 1
#     total = n * (n + 1) // 2
#     actual_sum = sum(arr)
#     return total - actual_sum

# Example usage
# arr = [1, 2, 4, 6, 3, 7, 8]  # 5 is missing
# missing = find_missing_number(arr)
# print("Missing number is:", missing)

# file1 = open('hello.txt','r')
# print(file1.read())
# file1.close()

# file2 = open('hello,txt','w') #overwrite
# file2.write('i love python')
# file2.close()

# file3 = open('xd.txt','a')
# file3.write('\nwelcome to my class guys')
# file3.close()

# pat ="C:\\Users\\USER\\OneDrive\\Desktop\\Python\\assignmentjuly2.py"

# with open(pat,'r') as f:
    # print(f.read())

# filez = open(pat,'r')
# import os
# pat = "C:\\Users\\USER\\OneDrive\\Desktop\\Python\\assignmentjuly2.py"

# if os.path.exists(pat):
#    print('path exists')
#    if os.path.isfile(pat):
#      print('its a file')
#    elif os.path.isdir(pat):
#      print('its a folder')
# else:
#    print('No!')



# homework
# quizapp with timer using function

# 5 function

#hangman game

# avesham

# _ _ _ _ _ _ _ _

#enter your letter : - e

# a _ e _ _ a _

# letters = ('avesham')

# letters = random.choice(letters)
# guessed letters = []
# tries = 5

# print("welcome to hangman!")
# print("_" * len(letter))

# while tries > 0:
#     guess = input("\nguess a letter: ").lower()

#     if  not guess.isalpha() or len(guess) != 1:
#         print("enter asingle alphabet letter.")
#         coninue