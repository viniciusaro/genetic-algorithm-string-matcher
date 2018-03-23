import random
from classes.DNA import DNA

class Population:

	individuals = []

	def __init__(self, size, target):
		for i in range(size):
			self.individuals.append(DNA(target))

	def isEvolved(self):
		for individual in self.individuals:
			if individual.fitness() == 1:
				print(''.join(individual.genes))
				return True
		return False

	def nextGeneration(self):
		print("yo")
		self.createWeightedPopulation()

	def createWeightedPopulation(self):
		weighted = []
		for individual in self.individuals:
			n = individual.score()
			for i in range(n):
				weighted.append(individual)

		return weighted
