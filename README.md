# Special button clicker
Way to often meet with math problems like this one:

> Mathew has a special calculator, that only has the buttons x2, -7, +13, ÷3. In the beginning, there is the number 4 on the display. How can he get the number 5 on the display, using exactly 5 moves?

Basically, the only way to solve this problem is brute force (wich is lenthy and boring) - or writing a program like this one, that will solve it for you.

## Parameters
`step_min`- the minimal amount of operations the special calculator can make
`step_max`- the maximal amount of operations the special calculator can make
`starting_number`- the number on the display in the beginning
`ending_number`- the number on the display in the end
* When given, the program displays the shortest way to get to that number
* When not given, the program displays all the possible numbers that could be on the display in the end

`steps_can_repeat`- whether or not we can use a function (push a button on the calculator) more than once

## Calculator.py

