#iterator are methods that are used to iterate collections like list, tuples etc.

P_n_list = [1,2,3,4,5,6,7]
Pn_iterator = iter (P_n_list)
print(next(Pn_iterator))
print(next (Pn_iterator))
print("*"*60)

for num in Pn_iterator:
    print(num)

    
