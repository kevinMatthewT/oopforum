from OOPclass import shopping

def MakeList():
    ShoppingList=[]
    items=eval(input("How many items will you order today?"))
    while items<1:
        print("Number of items must be at least 1.")
        items=eval(input("How many items will you order today?"))

    for i in range(items):
        x=i+1
        print("item #",x,"-")
        name=input("Enter food:")
        weight=eval(input("Enter amount of pounds:"))
        while weight<=0:
            print("Amount of pounds must be greater than 0.")
            weight=eval(input("Enter amount of pounds:"))
        foodinfo=shopping(name,weight)
        ShoppingList.append(foodinfo)
    
    return ShoppingList

def DisplayList(List_of_food):
    print("Here's a summary of the items purchased:"+"\n"+"----------------------------")
    for item in List_of_food:
        print(item.__str__())

def TotalAmt(List_of_food):
    total=0
    for item in List_of_food:
        total = total +item.cost()
    return total

def checklist():
    ShoppingList=MakeList()
    DisplayList(ShoppingList)
    TotalAmt(ShoppingList)


checklist()
