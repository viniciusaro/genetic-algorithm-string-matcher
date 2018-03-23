import string
import random
from classes.population import Population


TARGET = "Hello world"
POPULATION_SIZE = 100
MUTATION = 0.01

# Setup
population = Population(POPULATION_SIZE, TARGET)



# Draw
while population.isEvolved() == False:
	population.nextGeneration()