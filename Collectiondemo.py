from collections import namedtuple, deque, ChainMap, Counter,OrderedDict,defaultdict

courses = namedtuple('course',['name','tech'])
print(courses)
clist = courses(name= 'Data Science', tech = 'Python')
print(clist)
print(getattr(clist,"tech"))
print(clist.name)
print(clist[0])
courselist=['web Development', 'Angular']
print(courses._make(courselist))

"""-------------------------------------------------"""

#Deque - it is optimized list to perform insertion and deletion easily

t_list = ["Hardrik","Rohit","Pandya","Raina","Dhoni"]
tdeque= deque(t_list)
print("Original",tdeque)
tdeque.append("Virat")
print("Changed - ",t_list)











