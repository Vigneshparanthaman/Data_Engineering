"""
type_of_accounts = ("Savings", "current","Timing","Date")
print(type(type_of_accounts),type_of_accounts)
print("no of values on tuple ", len(type_of_accounts))

for i in type_of_accounts:
    print (i)

print("*"*50)

print( type_of_accounts.count("current"))
print(type_of_accounts.index("current"))
print(type_of_accounts[::-1])

print (type_of_accounts[1:3])
print (tuple(sorted(type_of_accounts)))
a = tuple(sorted(type_of_accounts))
print(a[::-1])
t_a = ("Savings",)
print(type(t_a))
"""

"""
wc_teams = ["India","Bangladesh","Australia","Pakistan","Newzeland","England"]
wc_wins= [2,0,5,1,0,1]
print(type(wc_teams),wc_teams)

wc_teams.append("Srilanka")
print(wc_teams)

wc_teams[4]= "Scotland"
print(wc_teams)

wc_teams.insert(1,"china")
print(wc_teams)
print(wc_teams.sort())
print("-"*10)
print(sorted(wc_teams))
"""
"""
class calculator:
    def add(self,num1,num2):
        return num1+num2

calculator = calculator()
num1= float(input("First number to add: "))
num2= float(input("Second number to add: "))
sum = calculator.add(num1,num2)
print("The ans of adding " , num1 ,"and ",num2, "is", sum)
"""
""" -------------------------------------------------------------------------------"""
"""
import random 

random_number = random.randint(1,100)
print("Random number: ",random_number)
"""
"""---------------------------------------------"""
"""
import random
random_number = random.random()
print("Random number from the 0 to 1 :" , random_number)
"""
"""----------------------------------------------------"""
"""
import random
start_range = 0
end_range = 10
num_number = 10
random_number = random.sample(range(start_range,end_range),num_number)
print("The list of random numbers are: ", random_number)
"""
"""---------------------------------------------------------"""
"""
Year = int(input("Year = "))

if Year % 4 ==0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print (Year ," is a leap year")
        else:
            print (Year ," is not a leap year")
    else:
        print (Year ," is a leap year")
else:
    print (Year ," is not a leap year")
-------------------------------------------------------"""
"""
wc_teams = ["India","Bangaladesh","Pakistan","Saudi Arabia","England"]
wc_wins=[1,2,1,3,0,]

print(type(wc_teams),wc_teams)

wc_teams.append("Srilanka")
print(wc_teams)
wc_teams.insert(2,"Australia")
print (wc_teams)
"""
i_players = ["Rohit","Virat","Rahul","Hardrik"]
a_players= ["Warner","kumble","Russal","Imran"]

team= [i_players,a_players]
print(team)
print(team[0])
print(team[1])
print(team[0][2])
jointeams=":".join(i_players)
print(jointeams)

i_players.append("gobi")
print(i_players)

i_players.extend(["Gayu","Kamatchi"])
print(i_players)

i_players.pop()
print(i_players)
    
















