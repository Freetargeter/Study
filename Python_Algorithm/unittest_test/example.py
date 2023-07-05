def my_example_function():
  print("Hi")
  
  name = input("Tell me your name")
  animal = input("Tell me your favorite animal")
  
  print("Hi {}, you like {}!".format(name, animal))

if __name__ == "__main__":
  my_example_function()