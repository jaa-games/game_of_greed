class Banker:
  def __init__(self, shelved = 0,balance=0):
        self.shelved = shelved
        self.balance=balance
  def shelf(self, num):
    """
        Will temporarily store unbanked points
        Argument:
        is the amount of points (integer) to add to shelf.
    """
    self.shelved +=num
    return self.shelved
  def bank(self):
      self.balance+= self.shelved
      self.shelved=0
      return self.balance
  def clear_shelf(self):
      self.shelved=0

