class Dentaku():
  def __init__(self):
    self.first_term = 0
    self.second_term = 0
    self.result = 0
    self.operation = ""

  def do_operation(self):
    if self.operation == "+":
      self.result = self.first_term + self.second_term
    elif self.operation == "-":
      self.result = self.first_term - self.second_term
    elif self.operation == "*":
      self.result = self.first_term * self.second_term
    elif self.operation == "/":
      self.result = self.first_term / self.second_term

dentaku = Dentaku()
while True:
  f = int(input("First_term "))
  dentaku.first_term = f
  o = input("Operation ")
  dentaku.operation=o
  s = int(input("Second_term "))
  dentaku.second_term=s
  dentaku.do_operation()
  r = dentaku.result
  print("Result ", r)