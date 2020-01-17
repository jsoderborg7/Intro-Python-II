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

  def add_player_item(self, item):
    self.inventory.append(item)
    item.on_pickup()

  def remove_player_item(self, item):
    self.inventory.remove(item)
    item.on_drop()
