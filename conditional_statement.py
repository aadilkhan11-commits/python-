# conditional statement
#if-elif-else


# age=21
# if(age>=18):
#     print("can vote")
# else:
#     print("cannot vote")

# light="green"
# if(light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("go")
# elif(light=="yellow"):
#      print("look")
# else:
#      print("light is fuck")



# num=5
# if(num>7):
#     print("greater than 7")
# elif(num>8):
#     print("greater than 8")
# else:
#      print("greater number")


# marks=int(input("enter student marks:"))
# if(marks>=90):
#     grade="A"
# elif(marks>=80 and marks<90):
#     grade="B"  
# elif(marks>=70 and marks<80):
#     grade="C"
# else:
#     grade="D"
# print("grade of the student ->",grade)    

#nesting
# if(cond):
#     if(cond2):
#         print()

# age=34
# if(age>=18):
#   if(age>=80):
#       print("cannot drive")
#   else:    
#    print("can drive")
# else:
#    print("cannot drive")

# match case


# print('''
#       +add
#       -sub
#       *mul
#       /div
#      ''' )
# num1=eval(input("enter the value:"))
# num2=eval(input("enter the val2:"))
# userCh=input("enter the user choice:")#+,-,/,*

# match userCh:
#     case '+':
#         print(num1+num2)
#     case '-':
#          print(num1-num2)
#     case '*':
#          print(num1*num2)
#     case '/':
#            print(num1/num2)
#     case _:
#            print("invalid opr")    

#check postive negative and zero of number

# num=eval(input("enter a number:"))
# if num>0:
#      print(num,"positive number")
# elif num==0:
#     print(num,"zero")
# else:
#      print(num,"negative number")


# leap year

# year=eval(input("enter the year:"))

# if(year%4==0 and year%100!=0):
#     print(year,"leap year")
# else:
#     print(year,"Not a leap year")


#check if a number is divisible by both 3 and 5

# num=eval(input("enter the number:"))
# if(num%3==0 and num%5==0):
#     print(num)



num1=eval(input("enter the value:"))
num2=eval(input("enter the val2:"))
userCh=input("enter the user choice:")
if userCh=="+":
    print(num1+num2)
elif userCh=="-":
    print(num1-num2)
elif userCh=="*":
    print(num1*num2)
else:
    print("invalid operation")





 



    
