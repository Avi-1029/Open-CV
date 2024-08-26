class Food:
    #constructor
    def __init__(self, healthy, veg, cuisine):
        self.healthy = healthy
        self.vegetarian = veg
        self.cuisine = cuisine
        
    def desc(self):
        print(' Healthy:', self.healthy,'\n Vegetarian:', self.vegetarian,'\n Cuisine:',self.cuisine, '\n' )
      
chickenburger = Food('No','No','American')
print(chickenburger.healthy)
print(chickenburger.vegetarian)
print(chickenburger.cuisine)

chickenburger.desc()

sushi = Food('Yes', 'Depends', 'Asian')

sushi.desc()