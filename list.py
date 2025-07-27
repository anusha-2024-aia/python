my_list=[10,20,30,40,50]
print(my_list[0])
print(my_list[::-1])
print(my_list.remove[0])
print(my_list)
print("\n")
print("squares of list:")
squares=[x*x for x in range(5)]
print(squares)
print("\n")
nested_list=[[1,2],[3,4]]
print(nested_list[0][1])

print("\n")
print("print all items in a list:")
lis=[1,2,3,4,5]
for item in lis:
    print(item)

print("\n")
print("The sum of all numbers in a list:")
list=[2,3,4,9,8]
sum=0
for num in list:
    sum+=num
print(sum)
print("\n")
print("Count how many times an item appears:")
my_list=[1,3,4,5,6,7,8,5,6,7]
count=my_list.count(5)
print(count)
print("\n")
print("remove duplicates froma list:")
list=[1,1,2,2,3,4,5,5]
unique=""
for num in list:
    if num not in unique:
        unique.append(num)
print(unique)
print("\n")
largest_num=[15,27,9,10,55]
print(max(largest_num))                

