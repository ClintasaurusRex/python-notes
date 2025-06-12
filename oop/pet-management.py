

class Pet: 
  def __init__(self, name, species, age, breed):
    
      self.name = name   
      self.species = species
      self.age = age
      self.breed = breed
      self.health = 100 
      self.hungry = True

  def feed(self):
     if self.hungry:
        print(f'{self.name} is being fed.')
        self.hungry = False
     else:
        print(f'{self.name} is not hungry right now')

  def give_medicine(self):
     if self.health < 100:
        self.health = min(100, self.health + 10)
        print(f'{self.name} has taken medicine. Health is now {self.health}')
     else:
        print(f'{self.name} is nice and healthy')

  def birthday(self):
     self.age += 1
     self.hungry = True
     print(f'Happy birthday {self.name}! You are now {self.age } years old')

  def status(self):
     print(f'Name: {self.name}')
     print(f'Species: {self.species}')
     print(f'Age: {self.age}')
     print(f'Breed: {self.breed}')
     print(f'Health: {self.health}')
     print(f"Hungry: {'Yes' if self.hungry else 'No'}")   

my_pet = Pet("Buddy", "Dog", 3, "Golden Retriever")
my_pet.status()
my_pet.feed()
my_pet.give_medicine()
my_pet.birthday()
