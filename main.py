ordernumber = 1;
def CafeMenu():
  print(f'\033[1m\033[95mOrder #{ordernumber}\033[0m')
  menu =  {"1": 3.5, "2": 3.5, "3": 3.5, "4": 3.5, "5": 2.25, "6": 0.75, "7": 0.75, "8": 0.75, "9": 0.5, "10":0.5, "11":0.5, "12": 1, "13": 1.75, "14": 1.5, "15": 2.5}
  orders = []
  ##while the amounts list is technically useless to the code, this can be used to send off to the Kitchen staff, along with the above orders tag and order number, useful for an actual restraunt scenario rather then just price calcs.
  amounts = []
  cost = 0;
  menulist = " 1 - Whole Meal Meat Burger: 3.5\n 2 - White Meat Burger: 3.5\n 3 - Whole Meal Vegetarian Burger: 3.5\n 4 - White Vegetarian Burger: 3.5\n 5 - All Salads: 2.25\n 6 - Cucumber: 0.75\n 7 - Lettuce: 0.75\n 8 - Tomato: 0.75\n 9 - Mustard: 0.5\n 10 - BBQ Sauce: 0.5\n 11 - Tomato Sauce: 0.5\n 12 - With Drink: 1\n 13 - Drink: 1.75\n 14 - With Chips: 1.5\n 15 - Chips: 2.5\nType 'q' to see current order + menu"
  print(menulist)
  #First Order, then repeats 'next item'
  order = input('Place order here: ')
  if order:
    while order != "":
      #Again, to the actual code, this is useless - but in a restraunt scenario its quite helpful.
      if order == "q":
        print(menulist)
        print(f'\033[93mOrders:{orders}\nAmount:{amounts}\033[0m')
        order = input('Next Item: ')
      elif order in menu:
        orders.append(int(order))
        amount = input("Amount: ")
        while not amount.isdigit():
          amount = input("Invalid Amount, Amount: ")
        amounts.append(int(amount))
        cost += int(amount)*menu[order]
        order = input('Next Item: ')
      else:
        order = input('Invalid input, Item: ')
  # Final Cost
  print('======')
  print(f'\033[33mTotal comes to \033[1m${cost}\033[0m')
  print('======')

#Repeats code to new order
while True:
  CafeMenu()
  ordernumber = ordernumber + 1