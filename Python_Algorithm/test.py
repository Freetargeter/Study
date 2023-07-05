from baekjoon_10866 import solution
from tud_test_base import set_keyboard_input, get_display_output

def test1():
  set_keyboard_input(["15",
                      "push_back 1",
                      "push_front 2",
                      "front",
                      "back",
                      "size",
                      "empty",
                      "pop_front",
                      "pop_back",
                      "pop_front",
                      "size",
                      "empty",
                      "pop_back",
                      "push_front 3",
                      "empty",
                      "front"])
  solution()
  output = get_display_output()
  return output

# def test2():
#   set_keyboard_input(["4 5",
#                       "1 2 -1",
#                       "1 3 2",
#                       "1 4 3",
#                       "2 4 2",
#                       "3 4 1"])
#   solution()
#   output = get_display_output()
#   return output


print("{}".format(test1()))
# print("{}\n{}".format(test1(), test2()))