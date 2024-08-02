menu = {
    1:{"name":"Pizza" , "price": 100},
    2:{"name":"Burger" , "price": 200},
    3:{"name":"Cheese" , "price": 150}
    }
def display_menu():
    print("menu: ")
    for num,item in menu.items():
        #print (item['name'])
        #print (item['price'])
        #print (num)
        print (f"{num} - {item['name']} - {item['price']}")
display_menu()

Product_ordering = int(input("Enter the menu id: "))
order = []
if 
for num,item in menu.items():
    order.append(item)
print(order)
    
