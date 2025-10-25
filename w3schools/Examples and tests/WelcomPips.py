class Person:
	def __init__(self, name):
		self.name = name
	def greet(self):
		return "Hello, " + self.name
	def welcome(self):
		message = self.greet()
		print(message + " Welcome to our world!")
p1 = Person("Pips")
p1.welcome()
