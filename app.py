from math import *

# print(sqrt(4))
# print (str(4)+str(4))
# print (4+4)

# name = input("enter your name : ")
# print("welcome ", name)

# mood = input("what is in your mind : ")
# print(mood)
# change = input("which word do you want to change :")
# replaceWith = input("replace with :")
# print(mood.replace(change, replaceWith))

# names = ["raj", "tom", "tim", "sam", "jon"]
# print(names)
# print(names[2])
# print(names[1:3])
# print(type(names))
# print(type(names[0]))
# print(names[-1])

# countries = list(( "USA", "Nepal", "UK", "USA", "Wales", "USSR"))
# print(countries)
# countries.append("Nigeria")
# countries.insert(1,"Argentina")
# countries.remove("USSR")
# countries.reverse()
# print(countries)
# countries.pop()
# print(countries)
# countries.pop(2)
# print(countries)

# del countries
# print(countries)


# my_numbers = (2, 4, 6)
# my_numbers = tuple((2, 4, 6))
# print(len(my_numbers))
# print(type(my_numbers))

# def greeting(name):
#     print("hello " + name , "welcome")

# name = input("enter your name : ")
# greeting(name)

# def greeting(*names):
#     print("hello " + names[1] , "welcome")

# greeting("raj","jon")

# def greeting(name, surname):
#     print("hello " + name + " " + surname, "welcome")

# greeting(name ="raj",surname = "jon")

# def my_func() : 
#     return 4+6

# print(my_func(5,4))

# def my_func(num1,num2) : 
#     return num1+num2 

# print(my_func(5,4))


# def my_func(num1,num2) : 
#     return num1+num2 

# num1 and num2 is regards string
# num1 = input("enter the first number :")
# num2 = input("enter the second number :")
# print(my_func(num1,num2))

# def my_func(num1,num2) : 
#     return num1+num2 

# num1 = int(input("enter the first number :"))
# num2 = int(input("enter the second number :"))

# print(my_func(num1,num2))

# def my_func(num1,num2) : 
#     return num1+num2 

# num1 = int(input("enter the first number :"))
# num2 = int(input("enter the second number :"))

# print(my_func(num1,num2))

# def my_func(num1,num2) : 
#     if num1>num2:
#         return str(num1)+" is greater than "+str(num2)
#     elif num1<num2:
#         return str(num1)+" is smaller than "+str(num2)
#     else :
#         return str(num1)+" and 5"+str(num2)+"  are equal"

# num1 = int(input("enter the first number :"))
# num2 = int(input("enter the second number :"))

# print(my_func(num1,num2))

# def my_func(num) : 
#     if num%2 == 0:
#         return str(num)+" is even "
#     else :
#         return str(num)+" is odd"

# num = int(input("enter the first number :"))

# print(my_func(num))

# my_obj = {
#     "name":"raj",
#     "surname":"jon",
#     "age":30,
#     "isTall":True,
#     "fiends":["a", "b", "c", "d", "e"]
# }

# print(len(my_obj))
# print(my_obj)
# print(type(my_obj))
# print(my_obj["name"])

#  white loop
# i = 5
# while i >= 5 and i<=10:
#     print("i =",i)
#     i += 1

# i = 5
# a = []
# while i >= 5 and i<=10:
#     a.append(i*2)
#     a.append(i*3)
#     i += 1

# even = []
# odd = []
# for item in a:
#     if item%2 == 0:
#          even.append(item)
#     else:
#          odd.append(item)

# print("all",a)
# print("even",even)
# print("odd",odd)

# getting multiple from a range as list /for loop 
# nums = range(1,100)
# multiple_of_two = []
# multiple_of_three = []
# multiple_of_four = []
# multiple_of_five = []
# multiple_of_four_or_five = []
# multiple_of_four_and_five = []
# for num in nums:
#     if num%2 == 0:
#         multiple_of_two.append(num)
#     if num%3  == 0:
#         multiple_of_three.append(num)
#     if num%4  == 0:
#         multiple_of_four.append(num)
#     if num%5  == 0:
#         multiple_of_five.append(num)
#     if num%4 == 0 or num%5  == 0:
#         multiple_of_four_or_five.append(num)
#     if num%4 == 0 and num%5  == 0:
#         multiple_of_four_and_five.append(num)

# print(multiple_of_two)
# print(multiple_of_three)
# print(multiple_of_four)
# print(multiple_of_five)
# print(multiple_of_four_or_five)
# print(multiple_of_four_and_five)

# nums = range(100)

# for num in nums:
#     if num%2 == 0:
#         print(num)
#         break

# calculator 
# num1 = int(input("enter the num1 : "))
# num2 = int(input("enter the num2 : "))
# operator = input("enter the operator : ")
# if operator == "-" :
#     print("the difference is ", abs(num1-num2))
# elif operator == "+" :
#     print("the sum is ", num1+num2)
# elif operator == "/" :
#     print("the division is ", abs(num1/num2))
# elif operator == "*" :
#     print("the product is ", num1*num2)
# elif operator == "%":
#     print("the remainder is ", num1*num2)
# else:
#     print("the invalid operator")

# try except
# try:
#     x = int(input("enter the number : "))
#     print("x = ", x)
# except:
#     print("error")

# try except finally
# try:
#     x = int(input("enter the number : "))
#     print("x = ", x)
#     print("x = ", y)

# except ValueError:
#     print("Value error input value is supposed to be integer")
# except NameError:
#     print("NameError trying to access a varaible which is not defined")
# finally:
#     print("the calculation is completed")

# reading external files
# countriesFile = open("countries.txt","r")
# for country in countriesFile.readlines():
#     print(country) 
# countriesFile.close()

# writing external files
# countriesFile = open("countries.txt","w") 
# countriesFile.write("Japan\n")
# countriesFile.write("America\n")
# countriesFile.write("Denmark\n")
# countriesFile.write("Portugal\n")
# countriesFile.close()

# testFile = open("test.txt","w") 
# testFile.write("This is a\n TEST FILE")

# appending in file
# testFile = open("test.txt","a") 
# tests = ["test1","test2","test3","test4","test5","test6",]
# for test in tests:
#     testFile.write("\n This is appending "+test)

# writing py file
# testFile = open("test.py","a") 
# tests = ["test1","test2","test3","test4","test5","test6",]
# for test in tests:
#     testFile.write("\nprint('hello')")

# class Test_class:
#     num = 5

# CopyClass = Test_class()
# print(CopyClass.num)

# class Person:   
#     def __init__(info, name, surname, age):
#         info.name = name
#         info.surname = surname
#         info.age = age

# person1 = Person("Ras", "Beri", 26)
# person2 = Person("Jon", "Di", 29)
# print(person1.name)
# print(person2.name)
    

# inheritance
# from student import Student

# class Person(Student):
#     pass
# person1 = Person(Student)
# print(person1.name)
# print(person1.age)

import newModule

newModule.testModule()