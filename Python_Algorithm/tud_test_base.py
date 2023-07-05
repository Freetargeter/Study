import builtins
import sys

input_values = []
print_values = []


def mock_input(s="", end=""):
    if s != "": print_values.append(s)
    return input_values.pop(0)


def mock_input_output_start():
    global input_values, print_values

    input_values = []
    print_values = []
    
    def temporaryPrint(*s, end=""):
      print_values.extend(s)

    builtins.input = mock_input
    sys.stdin.readline  = mock_input
    builtins.print = temporaryPrint


def get_display_output():
    global print_values
    return print_values


def set_keyboard_input(mocked_inputs):
    global input_values

    mock_input_output_start()
    input_values = mocked_inputs