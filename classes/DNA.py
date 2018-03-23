import random
import string

class DNA:
	genes = []
	target = ""
	population = string.ascii_uppercase + ' '

	def __init__(self, target, value=""):
		size = len(target)

		if len(value) > 0:
			self.genes = list(value.upper())
		else:
			self.genes = list(random.choices(self.population, k=size))
		self.target = target

	def score(self):
		targetArray = list(self.target)
		score = 0

		for i in range(len(targetArray)):
			if targetArray[i] == self.genes[i]:
				score = score + 1

		return score

	def crossover(self, other, mutationRate=0.0):
		size = len(self.genes)
		midpoint = random.randint(0, size - 1)
		newGenes = []

		for i in range(size):
			if random.random() < mutationRate:
				newChar = ''.join(random.choices(self.population, k=1))
				newGenes.append(newChar)
			else:
				if i < midpoint:
					newGenes.append(self.genes[i])
				else:
					newGenes.append(other.genes[i])

		return DNA(self.target, ''.join(newGenes))

	def fitness(self):
		return self.score() / len(self.target)

	def value(self):
		return ''.join(self.genes)
