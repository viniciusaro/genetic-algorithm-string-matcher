import random
from classes.DNA import DNA

class Population:
	individuals = []
	generations = 0
	mutationRate = 0

	def __init__(self, size, target, mutationRate):
		self.mutationRate = mutationRate
		for i in range(size):
			self.individuals.append(DNA(target))

	def isEvolved(self):
		for individual in self.individuals:
			if individual.fitness() == 1:
				return True
		
		return False

	def nextGeneration(self):
		self.generations += 1
		selectedPopulation = self.selectPopulation()
		self.reproduce(selectedPopulation, self.mutationRate)

	def selectPopulation(self):
		selected = []
		for individual in self.individuals:
			n = individual.score()
			for i in range(n):
				selected.append(individual)

		return selected

	def reproduce(self, selectedPopulation, mutationRate=0):
		populationSize = len(self.individuals)
		selectedPopulationSize = len(selectedPopulation)

		for i in range(populationSize):
			randomA = random.randint(0, selectedPopulationSize - 1)
			randomB = random.randint(0, selectedPopulationSize - 1)
			parentA = selectedPopulation[randomA]
			parentB = selectedPopulation[randomB]
			child = parentA.crossover(parentB, mutationRate)
			self.individuals[i] = child

	def printGeneration(self):
		fitest = self.fitest()
		print("Generation #", self.generations, "- best match:", fitest.value(), fitest.fitness())

	def printPopulation(self):
		for individual in self.individuals:
			print(individual.value(), individual.fitness().value())

	def fitest(self):
		fitest = None
		fitestFitness = 0
		for individual in self.individuals:
			if individual.fitness() > fitestFitness:
				fitest = individual
				fitestFitness = individual.fitness()
		
		return fitest

