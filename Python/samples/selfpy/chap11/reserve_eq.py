class Person:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname
    
  # 氏/名ともに等しければ同値とする
  def __eq__(self, other):
    if isinstance(other, Person):
      ''' 書き換え可能 
      return self.firstname == other.firstname and self.lastname == other.lastname
      '''
      return self.__dict__ == other.__dict__
    return false
    
  
if __name__ == '__main__':
  p1 = Person('太郎', '山田')
  p2 = Person('次郎', '鈴木')
  p3 = Person('太郎', '山田')
  print(p1 == p2)
  print(p1 == p3)