class Food:
    def __init__(self, healthy, veg, cuisine):
        self.healthy = healthy
        self.vegetarian = veg
        self.cuisine = cuisine

    def desc(self):
        print(' Healthy:', self.healthy,'\n Vegetarian:', self.vegetarian,'\n Cuisine:',self.cuisine, '\n' )

class Fruit(Food):
    def __init__(self, healthy, veg, cuisine, name, colour, country):
        Food.__init__(self, healthy, veg, cuisine)
        self.name = name
        self.colour = colour
        self.country = country

    def details(self):
        print(' Healthy:', self.healthy,'\n Vegetarian:', self.vegetarian,'\n Cuisine:',self.cuisine, '\n' 'Name:',self.name,'\n Colour:', self.colour, '\n Country:', self.country, '\n')
    

dragonfruit = Fruit('Yes', 'Yes', 'NA', 'Dragonfruit', 'Pink and Gray', 'Mexico')

dragonfruit.details()

chickenburger = Food('NO', 'NO', 'american')
chickenburger.desc()
