print() # equvalent to \n
print("hello world") #hello world
print("hello", "world") #hello world ->default separated by space
print("hello", "world", sep="-") #hello-world
print("hello", "world", end="...") #hello world... default end with \n but can be changed using end=""
print("hello", "world", end="*") #hello world* 
print("apple", "banana", "mango", sep=",", end="*") #apple,banana,mango*
print(2+3) #5
print(2 * 3) #6
print(2 ** 3) #8 exponential 2^3
print(2. ** 3) #8.0
print(2. ** 3.)  #8.0
print(4/2) # return float  2.0
# double slash return integer regardless of type of number divided and divisor
print(1//2) # double slash return integer 0
print(4//2) #double slash return integer  2
print(6//2) #double slash return integer  3
print(7//2) #double slash return integer  3
# when both numbers are +  - rounding always goes to the higher integer. 
print(6. // 4) #1.0 
print(-6. // -4) #1.0 
# when one of a number is - rounding always goes to the lesser integer. 
print("# when one of a number is - rounding always goes to the lesser integer.")
print(-6 // 4) #-2
print(6. // -4) #-2.0

# remainder module %
print("# remainder module %")
print(5%2) #1
print(5%3) #2
print(14%5) #4
print(14%4.5) #0.5
print(12%4.5) #3.0

# addition
print("# addition")
print(-4+4) #0
print(-4+4.0) #0.0
print(-4.0+8) #4.0
print(8.0-4) #4.0

# subtraction
print("# subtraction")
print(-4-4) #0 
print(-4-4.0) #0.0
print(-4.0-8) #4.0
print(8.0-4) #4.0

# multiple 
print(2 + 3 * 5) #17
print(9 % 6 % 2) #1 from left to right: first 9 % 6 gives 3, and then 3 % 2 gives 1;
print(2**2**3) #256  = 2^(2^3) = 2^8 
print(-2**3) # -8 = -2 * -2 * -2
print(-3**2) #  9 = -3 * -3
print(2 * 3 % 5) #
print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))
print((-3) ** 2)

# 0. () 
# 1. **
# 2. +- unary next to the right of power operator bind more strongly
# 3. / // % *
# 4. + -

print(2 * 3 % 5) #1 = 6%5

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
print((5 * (12 + 100) / 26) // 2)
print((5 * 112 / 26) // 2)
print((5 * 4.) // 2)
print(20. // 2)

print((2 ** 4), (2 * 4.), (2 * 4))
print(16, 8.0, 8)

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print(-0.5, 0.5, 0, -1)

print((2 % -4), (2 % 4), (2 ** 3 ** 2))
print(  -2,  2, 512)

#['False', 'None', 'True', 'and', 'as', 'assert', 'break', 
# 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 
# 'is',  'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
# 'return', 'try', 'while', 'with', 'yield']


#Here is a short story:

# Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples. They were all very happy and lived for a long time. End of story.

# Your task is to:

# create the variables: john, mary, and adam;
# assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
# having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
# now create a new variable named total_apples equal to the addition of the three previous variables.
# print the value stored in total_apples to the console;
# experiment with your code: create new variables, assign different values to them, and perform various arithmetic 
# operations on them (e.g., +, -, *, /, //, etc.). Try to print a string and an integer together on one line, e.g., "Total number of apples:" and total_apples.

john = 3
mary = 5
adam = 6
print(john, mary, adam, sep=",")
total_apples = john + mary + adam
print("Total numbers of apples :", + total_apples)

sheep = 1
dog = 3
print("sheep ->", sheep, "dog ->", dog )
sheep += 1
dog -= 1
print("sheep ->", sheep, "dog ->", dog )
sheep += 1
dog -= 1
print("sheep ->", sheep, "dog ->", dog )

miles = 7.38
kilometers = 12.25
# 7.38 miles is 11.88 kilometers
# 12.25 kilometers is 7.61 miles
miles_to_km = miles  * 1.61
kilometers_to_mile = kilometers * 1/1.61
print(miles , "miles is " , round(miles_to_km, 2), "kilometers")
print(kilometers , "kilometers is " , round(kilometers_to_mile, 2) , "miles")

# calculating area of a rectangle
# length = 5
# breath =  4
# area = length * breath
# print("area = " , area)

# print("lets calculate area of rectangle")
# print("enter the length of the rectangle = ")
# length = input("length = ")
# print("enter the breath of the rectangle = ")
# breath = input("breath = ")
# print("area = " , int(length) * int(breath))

x = int(input("Enter a number: ")) # The user enters 2
print(x * "5")


var = 0  # Assigning 0 to var
print("'var != 0' =", var != 0)
 
var = 1  # Assigning 1 to var
print("'var != 0' =", var != 0)


n = int(input("enter your desired number ="))
answer = n >= 100
print("answer is ", answer)

# if else
weather = int(input(" Is the weather good? press 0 if not good and any other key if its good")) != 0
if weather:
    print("Yaaaah ,we are going out for walk")
else:
    print("The weather is not good so, let's not walk")

# if else
want_to_do = int(input(" What do you want to do today? 1. go out 2. watch movie 3. play outdoor 4. nothing"))
if want_to_do == 1:
    print("Lets go to the zoo")
elif want_to_do == 2:
    print("Lets watch 007")
elif want_to_do == 3:
    print("Lets play football")
else:
    print("Lets just rest")