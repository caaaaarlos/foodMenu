# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 22:14:56 2022

@author: carlos
"""

# //carlos vazquez

# //10-2-2022
# // Purpose: program displays a food menu to the use the 
# // allows the user to select five items, that are added together 
# // and displayed at the end as sub total and and total


#print greeting 
print("Welcome to Moutain view")
print("please make a selection")
#print menu items 

menu = ("1.pizza - 3.75",
'2.hot dog - 2.25',
'3.nachos - 3.25',
'4.cotton candy - 2.25',
'5.chips - 1.50',
'6.candy - 1.50',
'7.ice cream - 2.75',
'8.snow cone - 3.00',
'9.regular beverage - 2.00',
'10.large beverage - 2.50')
list(menu)
#present menu via list 
for x in range(10): 
    print(menu[x])
#option to allow user to end order 
continue_order = 1
total = 0 #setting total value to 0

cart = []
while continue_order != 0:
    option = int(input(" "))#input taker for 
    cart.append(option)
    if option >= 10:#menu opitions 1-10
        print('we do not serve that here')
        break
    elif option == 1:
        total = total + 3.75
        print("pizza - 3.75")
    elif option == 2:
        total = total + 2.25
        print("hot dog - 2.25")
    elif option == 3:
        total = total + 3.25
        print("nachos - 3.25 " )
    elif option == 4:
        total = total + 2.25
        print("cotton candy - 2.25 " )
    elif option == 5:
        total =  total + 2.25
        print("chips - 1.50 " )
    elif option == 6:
        total=total + 1.50
        print("candy - 1.50 ")
    elif option == 7:
        total =  total + 2.75
        print("ice cream - 2.75 ")
    elif option == 8:
        total =  total + 3.00
        print("snow cone - 3.00 " )
    elif option == 9:
        total =  total + 2.00
        print("regular beverage - 2.00 " )
    elif option == 10:
        total =  total + 2.25
        print("large beverage-2.50" )
    elif option == 0:#zero option ends order list 
        print("Sub total = " + str(total))
        tax = total * 0.02 # multiples total by 2%
        print("2% tax = " + str(tax)      )  # and displays 
        total=total+tax# adding tax price to total to create grand total
        print("grand total = " + str(total))#display grand total to user 

    




