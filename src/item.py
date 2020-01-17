class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def get_item_name(self):
    return self.name

  def on_pickup(self):
    print(f"You have picked up {self.name}")

  def on_drop(self):
    print(f"You have dropped {self.name}")