# Special button clicker
Way too often, I meet with math problems like this one:

> Mathew has a special calculator, that has only the buttons x2, -7, +13, ÷3. In the beginning, there is the number 4 on the display. How can he display the number 5, using exactly 5 moves?

Basically, the only way to solve this problem is trying all possibilities by hand (which is lenthy and boring) - or writing a program like this one, that will solve it for you.

## Demo

```bash
$ python .\calculator_with_argparse.py 5 5 --starting_number 4 --ending_number 5 -r -f calculator_functions        
{5: ['times_2', 'minus_7', 'times_2', 'plus_13', 'divide_by_3']}
```
...and you can verify `((((4 * 2) - 7) * 2) + 13) / 3` is `5` and we have clicked exactly five buttons.

## Parameters
`step_min`- the minimal number of operations\
`step_max`- the maximal number of operations\
`starting_number`- the number on the display in the beginning\
`ending_number`- the number that should be on the display at the end
- When specified, the program displays the shortest way to get to that number
- When not specified, the program displays all possible numbers that could be on the display at the end

`steps_can_repeat`- whether or not we can use a function (push a button on the calculator) more than once\
`functions`- a Python file implementing calculator's operations, see [defaults](calculator_functions.py) as an example.

## Files

### Calculator_with_argparse.py

Main tool solving the problem described above.\
Fully operational from the command line (uses the python library `argparse`).\
When called from the command line, you should first give as parameters two numbers for `step_min` and `step_max`.\
Then you can list the optionals:
* For `starting_number`, write `-s` and then the number you want to set the value of `starting_number` (default is 1)
* For `ending_number`, write `-e ` and then the number you want to set the value of `ending_number` to
* `steps_can_repeat` decides if a button can be pushed repeatedly (default is False), write `-r` if you want to set it to True
* `functions` is defaultly set to `calculator_functions.py`, to use a different file with function specifications, write `-f ` and then the name of the file (without the ending .py)

So, if we wanted the program to solve the math problem from the beginning, this is what we would write in the command line:\
`$ python3 calculator_with_argparse.py 5 5 -s 4 -e 5 -r -f calculator_functions`

### Calculator.py
Originally, I did not know `argparse` and solved the task in the standalone Python file `Calculator.py`. The functionality is the same.
But it has the parameters set at the beginning of the code - to change them, you have to change the code.
* The list `functions` is imported on the 5th line (defaultly from the file calculator_functions.py)
* The other parameteres are set on the lines 8-13 (and are defaultly set to solve the math problem from the beginning)

### Calculator_functions.py
This program does nothing on its own, it's meant to be imported (parameter `functions`).\
It defines several operations (functions) and a list of them named `functions`.\
By default, `functions` have the operations of the math problem from the beginning (that means x2, -7, +13, ÷3).\
You can create your own program instead of the default one, but you have to keep the format - mainly, the program has to define a list named `functions`, that contains nothing but functions, and each function has to input a number and output a number.
