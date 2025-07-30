print("if-elif-else example:")
num=int(input("Enter a number:"))
if num>0:
    print("The number is positive")
elif num<0:
    print("The number is negative")
else:
    print("the number is zero")

print("\n")
print("netsed if example:")
age=15
if age >=18:
    print("you are eligible for voting")
    if age >=15:
        print("You are not eligible for voting")
else:
    print("Invalid age")

print("\n")
print("largest of three numbers:")
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))
if num1>=num2 and num>=num3:
    print("the largest num is, num1")
elif num2>=num1 and num2>num3:
    print("the largest num is , num2")
else:
    print("the largset num is, num3")

print("\n")
print("grade system:")
marks=int(input("enter the marks:"))
if marks>=90:
    print("grade A")
elif marks>=80:
    print("grade B")
elif marks>=70:
    print("grade C")
elif marks>=60:
    print("Grade d")
else:
    print("invalid marks")

print("\n")
print("Check if a year is a leap year:")
year=int(input("Enter a year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("year is a leap year")
else:
    print("year is not a leap year")

print("\n")
print("check if a number is prime:")
num = int(input("Enter a number:"))
if num>1:
    for i in range(2, int(num**0.5) +1):
        if(num%i)==0:
            print(num , "is not a prime number")
            break
        else:
            print(num, "is a prime number")
else:
     print(num, "is a prime number")
              