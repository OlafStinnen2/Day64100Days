class animal:
  species = None
  name = None
  sound = None
 
  def __init__(self, name, species, sound, color): # Include the 'self' in the 'init'
    self.name = name
    self.species = species
    self.sound = sound
    self.color = color

class bird(animal):

 def __init__(self):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = "green"


cow = animal("Ermintrude", "Bo Taurus", "Moo", "black")
print(cow.sound)



