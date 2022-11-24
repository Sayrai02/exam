product = []
product2 = []

def enter_p():
    x = input("enter a product" )
    return x

def add_p(p):
    y = enter_p()
    p.append(y)
    add_another_p()

def display_p():
    print(f'the products are :{product}')    
display_p()

def add_another_p():
    z = input("enter Y to add another or N exist")
    if z == "Y":
        add_p(product)
    elif z =="N" :
        display_p()
    else:
        print ("invalid input")     
add_p(product)   

def to_lower_case():
    x = 0
    while x < len(product):
        y = product[x].lower()
        product2.append(y)
        x = x+1
to_lower_case()        

def search_product():
    x = input("search for product")
    y = x.lower()
    z = 0
    if y in product2[z]:
        count_item = product2.count(y)
        total = len(product2)
        print("number of " ,y , "is" , count_item)
        print("total number of items are", total)
    else:
        print("item not found")    
        z = z+1
search_product()        



