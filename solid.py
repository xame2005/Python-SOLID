from abc import abstractmethod, ABC

class Animal(ABC):
	def __init__(self, type_breeding, color, size, weight):
		self.type_breeding = type_breeding
		self.color = color
		self.size = size
		self.weight = weight

	def survive(self):
		pass

	def eat(self):
		pass

	def random_function():
		return 'random'

class Subspecie_Animal(Animal):

	def __init__(self, type_breeding, color, size, weight, subspecie):
		Animal.__init__(self, type_breeding, color, size, weight)
		self.subspecie = subspecie

class IRunner():
	@abstractmethod
	def run():
		pass
	
class Two_Legs_Runner(IRunner):
	def __init__(self, speed):
		self.speed = speed

	def run(self):
		return 'I am running with 2 legs with current speed: ' + str(self.speed)

class Four_Legs_Runner(IRunner):
	def __init__(self, speed):
		self.speed = speed

	def run(self):
		return 'I am running with 4 legs with current speed: ' + str(self.speed)

class Runner_Animal(Subspecie_Animal):
	def __init__(self, type_breeding, color, size, weight, subspecie, type_of_runner):
		Subspecie_Animal.__init__(self, type_breeding, color, size, weight, subspecie)
		self.type_of_runner = type_of_runner

'''
class Cheetah(Runner_Animal):
	def __init__(self, speed):
		self.four_legs = Four_Legs_Runner(speed)'''

def flutter():
	return 'I am fluttering'

class Flyer_Animal(Animal):
	def fly(self, type_of_flying):
		return type_of_flying

class Noisy_Animal(Animal):
	def make_sound(self):
		pass

class Sleepy_Animal(Animal):
	def sleep(self):
		pass

class Pooper_Animal(Animal):
	def poop(self):
		pass

if __name__ == '__main__':
	bird = Flyer_Animal('Mamal','yellow',14.5,0.5)
	print(bird.fly(flutter()))
	cheetah = Runner_Animal('Mamal','yellow',144.5,100.5, 'feline', Four_Legs_Runner(66))

	print(cheetah.type_of_runner.run())
