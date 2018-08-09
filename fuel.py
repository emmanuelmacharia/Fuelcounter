
import math

'''the fuelcounter converts mpg into litres per kilometer,it goes on to calculate how much you'll spend on fuel for your journey
'''
class Fuelcalculator:
    '''calculates the fuel and the price one would pay for fuel for a certain trip in kilometres
    Attributes:
    make: the make of the vehicle e.g. toyota, koenigsegg
    model: the vehicles model e.g. agera, GTR
    mpg: miles per gallon
    distance: the distance the trip would in kilometres
    price: the price of the fuel'''

    milesconstant = 1.609344
    litresconstant = 3.785412


    def __init__(self, make, model, mpg, distance, price):
        self.make = input('Which type of car are you using? (Nissan, Toyota, Mercedes): ')
        self.model = input('What is the model of the car you are using?(Xtrail, Land-cruiser, Premio): ')
        self.mpg = float(input('How many miles per gallon does the car consume(please enter a valid number e.g. 1, 10.5): '))
        self.distance =float(input('How far are you travelling? (in kiometres):  '))
        self.price = price
        price = 105.99

    #try: 
    #    if type(mpg) == type(float):
    #        print (" ")

    #    elif type(distance) == type(float):
    #        print ('working')
    #except: 
    #    print('The input you entered for the mpg and distance are invalid. Please try again')

    def mpg_to_kmplitre(self):
        '''convertes the miles/gallon into kilometres/litre'''
        kmpl = (self.mpg* self.milesconstant)/self.litresconstant
        return kmpl

    def fueluse(self):
        '''calculates the amount of fuel a car takes for a trip of distance (x)'''
        kmpl = (self.mpg* self.milesconstant)/self.litresconstant
        fuel_used = self.distance/kmpl
        return fuel_used

    def cost(self):
        '''calculaes how much it costs to get to that destination'''
        kmpl = (self.mpg* self.milesconstant)/self.litresconstant
        fuel_used = self.distance/kmpl
        totalcost = fuel_used * self.price
        return totalcost

#def fuelcounter(price):
#    '''takes in 1 parameter, the price of oil'''
    
#    autoMaker= input('Which type of car are you using? (Nissan, Toyota, Mercedes) ')
#    carModel= input('What is the model of the car you are using?(Xtrail, Land-cruiser, Premio) ')
#    cartype=autoMaker+' '+carModel
#    print(cartype)
#    mpg=float(input('how many miles per gallon does it use? (please specify a number between 1 and 100) '))
#    km_per_litre= (mpg*1.609344)/3.785412
#    print('your car does {0:.2f} kilometres for every litre it consumes'.format(km_per_litre))
#    distance=float(input('how far will you travel? (write the distance in numbers) '))
#    litres_used= (distance/km_per_litre)
#    cost=price*litres_used
#    print("you will need ksh{0:.2f} for the fuel for your entire trip. Safe journey!!".format(cost))


#fuelcounter(105.6)