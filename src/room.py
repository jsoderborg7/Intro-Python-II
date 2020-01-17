# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, items=[]):
    self.name = name
    self.description = description
    self.n_to = None
    self.s_to = None
    self.e_to = None
    self.w_to = None
    self.items = items

  def removeItems(self, item):
    self.items.remove(item)

  def addItems(self, item):
    self.items.append(item)


