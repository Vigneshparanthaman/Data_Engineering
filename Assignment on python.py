"""
A=input("provide the word: ")
if A == A[::-1]:
    print ("It's palinrome")
else:
    print ("It's not palinrome")





Msg= """ Next, let's create a redux to hold our application's state. In the src directory, create a new file called store.js. inside this file,
import the configurestore function from @redusjs/toolkit and your todoslice reducer. Then, use configure store to create the Redux store."""

print("letter in the MSG paragraph is ",len(Msg))

count = 0
for i in Msg:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        count += 1
print("Vowels count in Msg",count)

cnt = 0
for i in Msg:
    if i not in ['a','e','i','o','u','A','E','I','O','U']:
        cnt += 1
print("consonent count in Msg",cnt)

cnts = 0
for i in Msg:
    if i.isalpha():
        cnts += 1
print("Alpha count in Msg",cnts)
"""


type_of_accounts = ("Savings", "current","Timing","Date")
print(type(type_of_accounts),type_of_accounts)



















