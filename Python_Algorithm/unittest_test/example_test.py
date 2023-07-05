from example import my_example_function
from tud_test_base import set_keyboard_input, get_display_output

def test1():
  set_keyboard_input(["2 2",
                      "2 9",
                      "3 5"])
  
  my_example_function()
  
  output = get_display_output()
  
  assert output == ["Hi", "Tell me your name", "Tell me your favorite animal", "Hi Mauricio, you like dogs!"]


def test2():
  set_keyboard_input(["Davide", "cats"])
  
  my_example_function()
  
  output = get_display_output()
  
  assert output == ["Hi", "Tell me your name", "Tell me your favorite animal", "Hi Davide, you like cats!"]

if __name__ == "__main__":
  print(test1())
  print(test2())
  