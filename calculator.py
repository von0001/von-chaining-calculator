# el menú
def calculatorMenu():
    print("Hey, welcome to von's calculator!")
    print("Here's your options:")
    print("[1] - Continue")
    print("[2] - Exit")

def reTry():
    while True:
            menuChoice = str(input("")).lower()
            
            if menuChoice == "continue" or menuChoice == "1" or menuChoice == "exit" or menuChoice == "2":
                return menuChoice
            else:
                print("That is an invalid input. Please try again.")

def endMenu():
     if hasResult == True:
          print(f"Your previous total was: {total}")
          print("[1] - Continue with this result")
          print("[2] - Start Over")
          print("[3] - Exit")
          print("Please use numbers for this menu.")
          endChoice = str(input(""))
          return endChoice

def usePreviousResult():
            while True:
                if endChain == True:
                    break
                elif endChain == False:
                     print("Do you want to use the previous result?")
                     print("[1] - No")
                     print("[2] - Yes")
                     revResult = str(input("")).lower()
                     if revResult == "yes" or revResult == "1":
                          print("Okay, the previous total was set as the x value.")
                          return True
                     elif revResult == "no" or revResult == "2":
                          print("Okay, it has not been set.")
                          return False
                     else:
                          print("That is an invalid input. Please try again.")
                               
# modules

def numbers(x,y):
    x = float(input("Enter your first number: "))
    y = float(input("Enter your second number: "))
    return (x,y)

def userChoice():
    print("[1] - Add")
    print("[2] - Subtract")
    print("[3] - Divide")
    print("[4] - Multiply")
    print("[5] - Exponent")
    print("[6] - Modulo")

    while True:
            choice = str(input("")).lower()
            
            if choice == "add" or choice == "1":
                return "add"
            if choice == "subtract" or choice == "2":
                return "subtract"
            if choice == "divide" or choice == "3":
                return "divide"
            if choice == "multiply" or choice == "4":
                return "multiply"
            if choice == "exponent" or choice == "5":
                return "exponent"
            if choice == "modulo" or choice == "6":
                return "modulo"
            else:
                print("That is an invalid input. Please try again.")

def add(x,y):
    global total, hasResult, endChain
    total = x + y
    print(f"Your total is {total}")
    hasResult = True
    endChain = False
    return total

def subtract(x,y):
    global total, hasResult, endChain
    total = x - y
    print(f"Your total is {total}")
    hasResult = True
    endChain = False
    print(hasResult)
    return total

def multiply(x,y):
    global total, hasResult, endChain
    total = x * y
    print(f"Your total is {total}")
    hasResult = True
    endChain = False
    return total

def divide(x,y):
     global total, hasResult, endChain
     while y == 0:
        print("You cannot divide by zero.")
        y = float(input("Enter a valid number."))
     else:
        total = x / y
        print(f"Your total is {total}")
        hasResult = True
        endChain = False
        return total
     
def exponent(x,y):
     global total, hasResult, endChain
     total = x ** y
     print(f"Your total is {total}")
     endChain = False
     hasResult = True
     return total

def modulo(x,y):
     global total, hasResult, endChain
     total = x % y
     print(f"Your total is {total}")
     endChain = False
     hasResult = True
     return total
     

# variable
total = 0
x = 0 
y = 0
hasResult = False
endChain = False

# code

while True:
    if endChain == False:
         calculatorMenu()
         
         menuChoice = reTry()
         
         if menuChoice == "exit" or menuChoice == "2":
              print("Thank you for using/trying von's Calculator!")
              break
         
         if menuChoice == "continue" or menuChoice == "1":
              if hasResult == False:
                  x = float(input("Enter your first number: "))
                  y = float(input("Enter your second number: "))
         if hasResult == True:
               prevResultChoice = usePreviousResult()
               if prevResultChoice == True:
                    x = total
                    y = float(input("Enter your second number: "))
               
               if prevResultChoice == False:
                        x = float(input("Enter your first number: "))
                        y = float(input("Enter your second number: "))     
                
               choice = userChoice()
               if choice == "multiply":
                    multiply(x,y)
               elif choice == "add":
                    add(x,y)
               elif choice == "subtract":
                subtract(x,y)
               elif choice == "exponent":
                    exponent(x,y)    
               elif choice == "modulo":
                    modulo(x,y)
               elif choice == "divide":
                    divide(x,y)
               elif choice == "exit":
                    break  
               endChoice = endMenu()
    else:
         x = total
         y = float(input("Enter your second number: "))

         choice = userChoice()
         
         if choice == "multiply":
              multiply(x,y)
         elif choice == "subtract":
              subtract(x,y)
         elif choice == "modulo":
              modulo(x,y)
         elif choice == "divide":
              divide(x,y)
         elif choice == "exit":
              break
         elif choice == "exponent":
              exponent(x,y)
         elif choice == "add":
              add(x,y)
              
    
    if endChoice == "1":
        endChain = True
    if endChoice == "2":
        endChain = False
    if endChoice == "3":
         print("Thank you for using von's Calculator!")
         break