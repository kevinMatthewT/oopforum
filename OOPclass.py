class shopping:
    def __init__(self,food,amount):
        self.food=food
        self.amount=amount
        self.standardprice=0
        self.price=0

    def PriceList(self):
        if self.food=="Dry Cured Iberian Ham":
           self.standardprice=(177.80)
        elif self.food=="Wagyu Steaks":
           self.standardprice=(450.00)
        elif self.food=="Matsutake Mushrooms":
           self.standardprice=(272.00)
        elif self.food=='Kopi Luwak Coffee':
           self.standardprice=(306.50)
        elif self.food=="Moose Cheese":
           self.standardprice=(487.20)
        elif self.food=="White Truffles":
           self.standardprice=(3600.00)
        elif self.food=="Blue Fin Tuna ":
           self.standardprice=(3603.00)
        elif self.food=="Le Bonnotte Potatoes":
           self.standardprice=(270.81)
        else :
            self.standardprice=0
        
        return self.standardprice
    
    def cost(self):
        self.PriceList()
        self.price= self.amount* self.standardprice
        return self.price


    def __str__(self):
        self.PriceList()
        self.cost()
        return f'Item:{self.food} \n Amount ordered: {self.amount} pounds \n Price per pound :${self.standardprice} \n Price of order: ${self.cost} '
