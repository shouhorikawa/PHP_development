class Coordinate:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  # Coordinate同士の加算
  def __add__(self, other):
    return Coordinate(
            self.x + other.x,
            self.y + other.y
          )
  
  def __str__(self):
    return f'({self.x},{self.y})'
  
if __name__ == '__main__':
  # Coordinate同士を加算
  c1 = Coordinate(10, 20)
  c2 = Coordinate(15, 25)
  print(c1 + c2)