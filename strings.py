print("Vowels in a string:")
string="Anusha"
vowels="aeiouAEIOU"
count=0
for char in string:
    if char in vowels:
        count+=1
        print(f"{char} is vowel")
    else:
        print(f"{char} is constant")
print(count) 
print("\n")
print("Two strings are anagram:")
str1="listen"
str2="anusha"
if sorted(str1)==sorted(str2):
    print(f"{str1} and {str2} are anagram")
else:
     print(f"{str1} and {str2} are not anagram")   
print("\n")
print("Lower to Upper case:")
lower_string="yellow"
print(lower_string.upper())

print("\n")
print("Reverse a string:")
string="python"
print(string[::-1])
print("\n")
print("Check Palindrome:")
palindrome_string="madam"
reversed_string=palindrome_string[::-1]
if palindrome_string == reversed_string:
    print(f"{palindrome_string} is a plaindrome")
else:
    print(f"{palindrome_string} is not a palindrome")
print("\n")
print("Remove spaces from string:")
string="hello world"
remove_spaces=string.replace(" ", "")
print(f"{string} without spaces is {remove_spaces}")
print("\n")
print("Count words in a sentence:")
sentence="python is fun"
word_count=len(sentence.split())
print(f"The number of words in the sentence is){word_count}")

print("\n")
print("Find the longest word in a sentence:")
sentence="I love Python programming"
words=sentence.split()
longest_word=""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
        print(f"longets wird in the sentence is {longest_word}")
