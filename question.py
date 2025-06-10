unit=int(input("Enter the amount of units used: "))
price=0
if unit>0 and unit<=100:
    price=unit*5 
    print("Bill:",price)
elif unit>100 and unit<=200:
    price=(100*5)+((unit-100)*8) 
    print("Bill:",price)   
elif unit>200:
    price=(100*5)+(100*8)+((unit-200)*10) 
    print("Bill:",price)  
else:
    print("Enter a valid amount!")
