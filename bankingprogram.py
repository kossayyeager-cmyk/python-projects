def showbalance():
    print("*"*10)
    print(f"your balance is :{balance}")
    print("*"*10)
def deposit(bal):
    global balance
    print("*"*10)
    balance+=bal
    print("*"*10)
def withdraw(bal):
   global balance
   print("*"*10)

   balance-=bal
   print("*"*10)
balance=float(100000)
running = True
def func(action):
         global running
         match action:
           case 1:
               showbalance()
           case 2:
                
                amount=float(input("enter the amount you want to deposit:"))
                if amount>0 :
                 deposit(amount)
                else:
                     print("invalid insertion")
                     func(2)
                     exit()
           case 3:
                
                 amount=float(input("enter the amount you want to withdraw:"))
                 if amount>0 and amount <=balance :
                    withdraw(amount)
                 else:
                    print("invalid insertion")
                    func(3)
                    exit()
           case 4:
                 running= False
           case _:
                 print("invalid input ")




while running:
     print("banking program:")
     print("1 show balance")
     print("2 deposit")
     print("3 withdraw")
     print("4 exit")
     action=int(input("chose from (1 to 4):"))
     if (action>0 and action>=1 and action <=4):
         
        func(action)

     else:
      print("invalid action")
   
   