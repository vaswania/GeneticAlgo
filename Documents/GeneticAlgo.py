import math

import random

import numpy


#implementing genetic algorithm for optimizing cans


class Can:

    #initializes cans with radius, height, volume, area 
    def __init__(self, radius = None, height = None):

        self.radius = None

        self.height = None

        self.fitnessScore = 0;

        self.vol = 0;

        self.Area = 0;

        if radius is not None:

            self.radius = radius

        else:

            self.radius = int(random.randrange(1,25))

        if height is not None:

            self.height = height

        else:

            self.height = int(random.randrange(1,100))
        
    #calculating volume of can using the formula 3.14*r*r*h 
    def calcVolume(self):
 

        self.vol = 3.14 * float(self.radius) * float(self.radius) * float(self.height)

        return (self.vol)

    #calculating area of can using the formula 2*3.14*r*(r + h)

    def calcArea(self):

        self.area = 2 * 3.14 * float(self.radius) * (float(self.radius) + float(self.height))

        return(self.area)

    #calculating fitness of can using fitness function (Volume /Area) with constraint that volume has to be equal to or greater than 400

    def calculateFitness(self):

        self.vol = self.calcVolume()

        if(self.vol > 400):

            self.fitnessScore = (3.14* self.radius * self.radius * self.height)/((2 * 3.14 * self.radius * self.height)+(2 * 3.14 * self.radius * self.radius ))

            print("Volume is "+ str(self.vol))

            print("Fitness Score is" + str(self.fitnessScore))

        else:

            self.fitnessScore = 0

            print("Fitness Score is" + str(self.fitnessScore))


        return(self.fitnessScore)

class Population:

    #initializes population with radius, height, volume, area 
    def __init__(self):
     
        self.mutationRate = 0.01

        self.maxFitnessScore = 0 #initializing maximum fitness score as 0
 
        self.cans = list()
 
        self.parA = []

        self.parB = []

#	population size is 100 so adding new cans to the population
        for i in range(0, 100):

            self.cans.append(Can())

        self.matingPool = []; #initializing mating pool for selecting the parents

#obtains the can with highest fitness score

    def getFittest(self, gen = None):

        if (gen is None):

            for i in range(0, 100):

                self.cans[i].fitnessScore = self.cans[i].calculateFitness() #calculate fitness score 
                if (self.cans[i].fitnessScore > self.maxFitnessScore): #compare fitness with max

                    self.maxFitnessScore = self.cans[i].fitnessScore #update the max score 
                    print("maxFitnessScore " + str(self.maxFitnessScore)) #print the maxscore 
                    self.Fittest = self.cans[i]




            else:

                self.gen = gen

                for i in range(0, 100):

                    self.gen[i].fitnessScore = self.gen[i].calculateFitness() #calculate fitness score 
                    if (self.gen[i].fitnessScore > self.maxFitnessScore): #compare fitness with max

                        self.maxFitnessScore = self.gen[i].fitnessScore #update the max score 
                        print("maxFitnessScore " + str(self.maxFitnessScore)) #print the maxscore 
                        self.Fittest = self.gen[i]


            return self.Fittest
                              
        #normalizes fitness value by diving it by maximum fitness to get the probability of that individual (can) and then adds them to the mating pool based on that probability 
    
    def normalizeFitness(self):


        self.normFitnessScores = [] #initializing normalized fitness scores 
        mostFitCan = self.getFittest() #getting the fittest can 
        self.maxFitnessScore = mostFitCan.calculateFitness() 
        for i in range(0, 100):

            self.normFitnessScores.append(self.cans[i].calculateFitness()/self.maxFitnessScore) #filling normalized fitness scores

            self.probablityScore = self.normFitnessScores[i]*100 #multiply normalized scores by 100 to get probability

            for j in range (0, int(self.probablityScore)):

                self.matingPool.append(self.cans[i])	#fill	the	mating	pool	such	that	higher number of individuals with higher values of fitness are present (roulette wheel)


            print(str(len(self.matingPool)))


        print(str(self.normFitnessScores))

#selects individuals randomly from the mating pool for crossover 

    def naturalSelection(self):

        self.nextgen = []

        self.generation = 0

        for i in range(0, 2):

            if (self.generation < 1):

                self.parA = random.sample(self.matingPool, 100) #selection of parent 1 
                self.parB = random.sample(self.matingPool, 100) #selection of parent 2 
                self.child = self.crossover() #mating or crossingover to give the offspring 
                for j in range(0, 100):

                    self.nextgen.append(self.child[j])

                self.generation+=1 #incrementing value of generation for next generation
        

                self.fittestCan = self.getFittest(self.nextgen) #getting the fittest can for generation 
                print("Generation no " + str(self.generation)) #print generation number
                print ("radius " + str(self.fittestCan.radius)+ ", " "height " + str(self.fittestCan.height)) #print radius, height and fitness score of the fittest can

            else:

                numpy.random.shuffle(self.nextgen) #shuffling the next generation 
                self.parA = self.nextgen #next gen becomes the parent 
                numpy.random.shuffle(self.nextgen) #shuffling the next generation 
                self.parB = self.nextgen #nextgen becomes the parent

                self.child = self.crossover() # crossingover to give the offspring #filling next gen with new child 
                for j in range(0, 100):

                    self.nextgen.append(self.child[j])

                self.generation+=1 #incrementing value of generation for next generation 
                self.fittestCan = self.getFittest(self.nextgen) #getting the fittest can for generation 
                print("Generation no " + str(self.generation)) #print generation number
                print ("radius " + str(self.fittestCan.radius)+ ", " "height " + str(self.fittestCan.height)) #print radius, height and fitness score of the fittest can




#crossover in which genetic information of can is exchanged based on random number generation

    def crossover(self):

        self.child = []


    for i in range(0, 100):

        self.ch = random.randint(0,1) #randomly generating a number for crossover 
        self.child.append(Can())

    #incase the radius or height becomes 0 making it again between 5 and 25
    

    if(self.parA[i].radius == 0):

        self.parA[i].radius = random.randint(5, 25)

    if (self.parA[i].height == 0):

        self.parA[i].height = random.randint(5, 25)

    if (self.parB[i].radius == 0):

        self.parB[i].radius = random.randint(5, 25)

    if (self.parB[i].height == 0):

        self.parB[i].height = random.randint(5, 25)

    #for each random value different value generated whether value of r or h is chosen from particular parent is decided

    if (self.ch == 0): #if random number is 0

        self.child[i].radius = self.parA[i].radius #radius of parent A is selected 
        self.child[i].height = self.parB[i].height #height of parent B is selected 
        volofCan = 3.14 * self.child[i].radius * self.child[i].radius * self.child[i].height

        #calculate volume

        print("Volume of ch0" + str(volofCan))

    else:

        self.child[i].radius = self.parB[i].radius #radius of parent B is selected self.child[i].height = self.parA[i].height #height of parent A is selected volofCan = 3.14 * self.child[i].radius * self.child[i].radius * self.child[i].height

    #calculate volume

    print("Volume of ch1" + str(volofCan))

    return self.child


def mutate(self):

#mutating or changing value by swapping value of r with value of h for i in range(0, 100):

    for i in range(0, 100):
        if random.random() < self.mutationRate:

            self.cans[i].radius = self.cans[i].height

        print("Mutated")
 
print("Started")	#start the program

p = Population()	#initialize the population

p.mutate() #mutate population with mutation rate of 0.01

p.normalizeFitness()	#calculate fitness of the population and normalize fitness value

p.naturalSelection()	#selection based on fitness value and crossover to produce offspring

print("completed")



