# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
    self.inventory = []

  def __str__(self):
    return f"{self.name}"

# add and remove items from player inventory

  def addItem(self, item):
    self.inventory.append(item)
    item.pickup()

  def removeItem(self, item):
    self.inventory.remove(item)
    item.drop()
