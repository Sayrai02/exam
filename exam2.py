data=["1234","123456","1234567890","1234567","013","011","8543210","12345","1238974"]

x=[]
y=[]

def name():
    n=0
    while n < len(data):
        if len(data[n]) <=4:
            x.append(data[n])
        elif len(data[n]) >=7:
            y.append(data[n])
        n =  n +1
    z=(x, y) 
    print(z)
name()        


