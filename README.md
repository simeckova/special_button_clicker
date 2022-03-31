# Special button clicker
Way to often meet with math problems like this one:

> Mathew has a special calculator, that only has the buttons x2, -7, +13, ÷3. In the beginning, there is the number 4 on the display. How can he get the number 5 on the display, using exactly 5 moves?

Basically, the only way to solve this problem is brute force (wich is lenthy and boring) - or writing a program like this one, that will solve it for you.

## Parameters
`step_min`- the minimal amount of operations the special calculator can make\
`step_max`- the maximal amount of operations the special calculator can make\
`starting_number`- the number on the display in the beginning\
`ending_number`- the number on the display in the end
* When given, the program displays the shortest way to get to that number
* When not given, the program displays all the possible numbers that could be on the display in the end

`steps_can_repeat`- whether or not we can use a function (push a button on the calculator) more than once
`functions` is imported from another file, and is a list of functions that we can use as operations in our calculator

## Calculator_with_argparse.py
A program that solves the problem from the beginning.\
Fully operational from the command line (using the python library Argparse).\
When calling, you should first list numbers for `step_min` and `step_max`.\
Then you can list the optionals:
* For `starting_number`, write `-s ` and then the number you want to set the value to
    - It is defaultly set to 1
* For `ending_number`, write `-e ` and then the number you want to set the value to
* `steps_can_repeat` is defaultly False, write '-r' if you want to set it to True
* `functions` is defaultly set to calculator_functions.py, to use a different file, write `-f ` and the name of the file (without the ending .py)

So, if we wanted the program to solve the math problem from the beginning, this is what we would write in the command line:\
`$ python3 calculator_with_argparse.py 5 5 -s 4 -e 5 -r -f calculator_functions`

## Calculator.py
Similar functionality as Calculator_with_argparse.py\
But it has the parameters set at the beginning of the code - to change them, you have to change the code.
* The list `functions` is imported on the 5th line (defaultly from the file calculator_functions)
* The other parameteres are set on the lines 8-13 (and are defaultly set to solve the math problem from the biginning)

## Calculator_functions.py
This program does nothing on its own, it's meant to be imported.\
It first defines several functions, then defines a list `functions` that contains all the functions contained in the program.\
Defaultly, `functions` has the operations of the math problem from the beginning (that means x2, -7, +13, ÷3).\
You can create your own program instead of this one, but you have to keep the format - mainly, the program has to define a list named `functions`, that contains nothing but functions, and the functions have to input and output a number.
