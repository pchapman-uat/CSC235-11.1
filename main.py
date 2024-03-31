# A folder called colors stores the colored values, and the colored print functions
# from the coloredPrint file, import everything
# To have colored values printed PowerShell, VSCode terminal, or other terminals must be used
# ComandLine will NOT work with colored lines, and will display symboles instead
from colors.coloredPrint import *

# Create a class for the Items
class Item:
    # When the object is constructed set the values
    # If no color was provided, set to the default color of ANSI_RESET 
    def __init__(self, name, cost, color = ANSI_RESET):
        self.color = color
        self.name = name
        self.cost = cost
        self.color = color
    # Create a buy item function that accepts the money provided
    def buyItem(self, money):
        # Run the print item function to display the name with the color, as well as a green line for the cost of the item
        print(f"A {self.printItem()} will cost ${genGreenLine(str(self.cost))}")
        # Display how much money the user has
        print(f"You have ${genGreenLine(str(money))}")
        # If the user has enough money to buy the item
        if money > self.cost:
            # Set their remaining money to the difference
            reaminMoney = money - self.cost
            # Provide the moeny remaining, and ask for confirmation
            print(f"To buy {self.printItem()}, you will have ${genGreenLine(str(reaminMoney))} left")
            confirm = input("Please confirm (y/n)")
            # if the user selected "y"
            if(confirm == "y"):
                # Tell the user they bought the item, and return the remaining money
                print(f"You bought one {self.printItem()}")
                return reaminMoney
            # Else return none
            else:
                return None
    # Print the item name using the color
    def printItem(self):
        return genLine(self.color, self.name)

# using an array of choice, print them with the index
def printChoices(choicesArr):
    for i in range(len(choicesArr)):
        print(f"{i}: {choicesArr[i]}")
# Print all items in the invintory
def printItems():
    # Create variables to store the count of each item
    # This code can be simplified
    shovels = 0
    ropes = 0
    swords = 0
    if len(invintory) == 0:
        print("You have no items")
    # For each item in the invintory
    for item in invintory:
        # if the name is the same as the possible tool, update the count
        if item.name == posibleTools[0].name:
            shovels += 1
        elif item.name == posibleTools[1].name:
            ropes+= 1
        elif item.name == posibleTools[2].name:
            swords+=1
    # print the choices with colored lines for each item type
    printChoices([f"{genBlueLine("Shovles")} | x{shovels}", f"{genYellowLine("Ropes")} | x{ropes}",f"{genRedLine("Swords")} | x{swords}"])
# Array that stores all posible items for the user to buy
posibleTools = [Item("Shovel", 100, ANSI_BLUE), Item("Rope", 10, ANSI_YELLOW), Item("Sword", 150, ANSI_RED)]
# The users starting money
currentMoney = 500

# The users starting invintory
invintory = []

# A custom function that loops until the user inputs an int
def intInput(text):
    value = input(text)
    # Try converting to an int
    try:
        return int(value)
    # if failed loop the function
    except:
        print("Please enter a number")
        intInput(text)
# Main loop for the aplication
while True:  
    # Print 3 new lines
    print("\n"*3)
    # print the choices for the user to do 
    print("What would you like to do?")
    printChoices(["Buy item", "Sell item", "View Invintory", "Quit"])
    choice = intInput("")

    # IF the user inputed a 0 (Buy item)
    if choice == 0:
        # Print all items
        for i in range(len(posibleTools)):
            tool = posibleTools[i]
            print(f"{i}: {tool.printItem()}, ${tool.cost}")
        # Ask the user for the id of the item they want to buy
        itemNum = intInput("Please enter the id of the item you want to buy")
        # Get the item data for the selected item
        selectedItem = posibleTools[itemNum]
        # Run the buy item function from the selected item, providing the current money
        remaining = selectedItem.buyItem(currentMoney)
        # Function will return None if there is not enough money, so this if statment will only run if the user has money left over
        if remaining:
            # Add the item to the invintory
            invintory.append(selectedItem)
            # Update the current money
            currentMoney-=remaining
    # If the user selects 1 (Selling)
    elif choice == 1:
        # Print the users invintory
        printItems()
        #  Ask the the item they want to sell
        sellChoice = intInput("What item do you want to sell")
        # Loop through all items in the invintory
        # TODO: Checlk for incorrect ID
        for i in range(len(invintory)):
            # If the item name is the same as the possible item name...
            if invintory[i-1].name == posibleTools[sellChoice].name:
                # Remove the item from the list
                invintory.pop(i-1)
                # Break out of the for loop
                break

    # If the user selects 2 (Print invintory)
    elif choice == 2:
        # Check if there are items in the invintory
        if len(invintory) > 0:
            # Print all items
            printItems()
        # else print a red line showing that there are no items
        else:
            print(genRedLine("You have no items"))
    # If the user selcts 3, break out of the loop ending the program
    elif choice == 3:
        break



