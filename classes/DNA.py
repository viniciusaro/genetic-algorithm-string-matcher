import random
import string

class DNA:
	genes = []
	target = ""

	def __init__(self, target):
		population = string.ascii_letters + ' '
		size = len(target)
		self.genes = list(random.choices(population, k=size))
		self.target = target

	def score(self):
		targetArray = list(self.target)
		index = 0
		score = 0
		for char in targetArray:
			gene = self.genes[index]
			if char == gene:
				score = score + 1
			index = index + 1

		return score

	def fitness(self):
		return self.score() / len(self.target)