import string
import random

from classes.population import Population

TARGET = "VINICIUS ALVES RODRIGUES"
POPULATION_SIZE = 1000
MUTATION = 0.01

# Setup
population = Population(POPULATION_SIZE, TARGET, MUTATION)

# Draw
while population.isEvolved() == False:
	
	population.printGeneration()

	population.nextGeneration()

print("")
print("Best individual", population.fitest().value())
print("Genes:", population.fitest().genes)
print("Number of generations: #", population.generations)