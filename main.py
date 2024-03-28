from colors.coloredPrint import *


class Item:
    def __init__(self, name, cost, color = ANSI_RESET):
        self.color = color
        self.name = name
        self.cost = cost
        self.color = color
    def buyItem(self, money):
        print(f"A {self.printItem()} will cost ${genGreenLine(str(self.cost))}")
        print(f"You have ${genGreenLine(str(money))}")
        if money > self.cost:
            reaminMoney = money - self.cost
            print(f"To buy {self.printItem()}, you will have ${genGreenLine(str(reaminMoney))} left")
            confirm = input("Please confirm (y/n)")
            if(confirm == "y"):
                print(f"You bought one {self.printItem()}")
                return reaminMoney
            else:
                return None
    def printItem(self):
        return genLine(self.color, self.name)


def printChoices(choicesArr):
    for i in range(len(choicesArr)):
        print(f"{i}: {choicesArr[i]}")

def printItems():
    shovels = 0
    ropes = 0
    swords = 0
    for item in invintory:
        if item.name == posibleTools[0].name:
            shovels += 1
        elif item.name == posibleTools[1].name:
            ropes+= 1
        elif item.name == posibleTools[2].name:
            swords+=1
    printChoices([f"{genBlueLine("Shovles")} | x{shovels}", f"{genYellowLine("Ropes")} | x{ropes}",f"{genRedLine("Swords")} | x{swords}"])

posibleTools = [Item("Shovel", 100, ANSI_BLUE), Item("Rope", 10, ANSI_YELLOW), Item("Sword", 150, ANSI_RED)]

currentMoney = 500


invintory = []

def intInput(text):
    value = input(text)
    try:
        return int(value)
    except:
        print("Please enter a number")
        intInput(text)

while True:  
    print("\n"*3)
    print("What would you like to do?")
    printChoices(["Buy item", "Sell item", "View Invintory", "Quit"])
    choice = intInput("")

    if choice == 0:
        for i in range(len(posibleTools)):
            tool = posibleTools[i]
            print(f"{i}: {tool.printItem()}, ${tool.cost}")
        itemNum = intInput("Please enter the id of the item you want to buy")
        selectedItem = posibleTools[int(itemNum)]
        remaining = selectedItem.buyItem(currentMoney)
        if remaining:
            invintory.append(selectedItem)
            currentMoney-=remaining
    elif choice == 1:
        printItems()
        sellChoice = intInput("What item do you want to sell")
        for i in range(len(invintory)):
            if invintory[i-1].name == posibleTools[sellChoice].name:
                invintory.pop(i-1)
                break

    elif choice == 2:
        if len(invintory) > 0:
            printItems()

        else:
            print(genRedLine("You have no items"))
    elif choice == 3:
        break



