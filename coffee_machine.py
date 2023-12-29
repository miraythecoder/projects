#!/usr/bin/env python
# coding: utf-8

# In[ ]:


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

earning=0
def payment():
    global earning
    print("Please insert coins.")
    quarters=int(input("How many quarters?: "))
    dimes=int(input("How many dimes?: "))
    nickles=int(input("How many nickles?: "))
    pennies=int(input("How many pennies?: "))
    total=0.25*quarters+0.10*dimes+0.05*nickles+0.01*pennies
    cost=MENU[order]["cost"]
    rem=total-cost
    remain=round(rem,2)
    if remain>=0:
        print(f"Here is 💲{remain} in charge.")
        print(f"Here is your {order}☕. Enjoy!")
        earning=earning+MENU[order]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded.")
        
def espre():
    resources['water']-=50
    resources['coffee']-=18
    
def latt():
    resources['water']-=200
    resources['milk']-=150
    resources['coffee']-=24
  
def capp():
    resources['water']-=250
    resources['milk']-=100
    resources['coffee']-=24
    
   
    
def show_resources():
    print(f"water: {resources['water']}ml\nmilk: {resources['milk']}ml\ncoffee: {resources['coffee']}mg")
    
def check():
    if order=="espresso":
        if resources["water"]<50:
            print("Not enough water")
        if resources["coffee"]<18:
            print("Not enough coffee")
        elif resources["water"]>=50 and resources["coffee"]>=18:
            payment()
            espre()
    elif order=="latte":
        if resources["water"]<200:
            print("Not enough water")
        if resources["milk"]<150:
            print("Not enough milk")
        if resources["coffee"]<24:
            print("Not enough coffee")
        elif resources["water"]>=200 and resources["milk"]>=150 and resources["coffee"]>=24:
            payment()
            latt()
    else:
        if resources["water"]<250:
            print("Not enough water")
        if resources["milk"]<100:
            print("Not enough milk")
        if resources["coffee"]<24:
            print("Not enough coffee")
        elif resources["water"]>=250 and resources["milk"]>=100 and resources["coffee"]>=24:
            payment()
            capp()
          

while True:
    order = input("What would you like? (espresso/latte/cappucino):")
    if order == "espresso" or order=="latte" or order=="cappuccino" :
        check()
        continue
    elif order == "report":
        show_resources()
        print(f"Money: {earning}")
        continue
    elif order == "off":
        break
    else:
        print("Your order is not included in the menu.")
        break
    

