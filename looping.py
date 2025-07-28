print("Print numbers 1 to 10")
for i in range(10):
    print(i)

print("\n")
for i in range(2,21,2):
    print(i,end=' ')
print("\n")
print("the sum of number is  1 to 100")
sum=0
for i in range(1,101):
    sum+=i
print(sum)

print("\n")
print("print each character in a string:")
string="anusha"
for i in range(0,6):
    print(string[i])

print("\n")
print("Create a new list using a loop:")
new_list=[]
for i in range(1,6):
    square=i*i
    print(square)  

print("\n")
print("While Loop:")
print("print even numbers from 1 to 20:")
num=2
while num <= 20:
    print(num)
    num+=2

print("\n")
print("print odd numbers from 1 to 20:")
num=1
while num<=20:
    print(num)
    num+=2

print("\n")
print("print each character in a string using while loop:")
string="anusha"
index=0
while index<=len(string):
    print(string[index])
    index+=1

print("\n")
print("create a list of squares from 1 to 5 using while loop:")
num_list=[]
i=1
while i <= 5:
    square=i*i
    i+=1
    num_list.append(square)
print(num_list)                

    
       