class FourCal:
  def __init__(self, first, second):
    self.first = first
    self.second = second
  def setdata(self, first, second):
    self.first = first
    self.second = second
  def add(self):
    result = self.first + self.second
    return result
  def mul(self):
    result = self.first * self.second
    return result
  def sub(self):
    result = self.first - self.second
    return result
  def div(self):
    result = self.first / self.second
    return result



a = FourCal(2, 4)

print(a.first)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())


# 매서드 상속
class MoreFourCal(FourCal):
  def pow(self):
    result = self.first ** self.second
    return result
  
a = MoreFourCal(4, 2)
print(a.pow())

# 매서드 오버라이딩
class SafeFourCal(FourCal):
  def div(self):
    if self.second == 0:
      return 0
    else:
      return self.first / self.second
    
a = SafeFourCal(4, 0)
a.div()

# 클래스 변수
class Family:
  lastname = "김"

print(Family.lastname)
a = Family()
print(a.lastname)
b = Family()
print(b.lastname)

Family.lastname = "박"

print(a.lastname)
print(b.lastname)

id(Family.lastname)
id(a.lastname)
id(b.lastname)

