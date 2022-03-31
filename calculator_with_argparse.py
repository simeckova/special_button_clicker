from itertools import permutations, product
from typing import Dict, List, Any, Optional, Set
import argparse
import importlib


# Start parameters:
parser = argparse.ArgumentParser()
parser.add_argument('step_min', type=int, help='minimal amount of steps')
parser.add_argument('step_max', type=int, help='maximal amount of steps')
parser.add_argument('-s', '--starting_number', type=int, default=1,
                    help='the number on the calculator at the start-default 1')
parser.add_argument('-e', '--ending_number', type=int,
                    help='the number on the calculator at the end, optional')
parser.add_argument('-r', '--steps_can_repeat', action='store_true',
                    help='include if steps can repeat')
parser.add_argument('-f', '--functions', default='calculator_functions',
                    type=str, help='file with possible functions to use as '
                    'steps, default = calculator_functions.py')
args = parser.parse_args()

functions = importlib.import_module(args.functions).functions

assert args.step_max >= args.step_min, (
    "step_max must not be smaller than step_min")
assert args.steps_can_repeat or args.step_min <= len(functions), (
    "step_min bigger than amount of available steps, and step repetition off")

plans: List[Any] = []
for step_num in range(args.step_min, args.step_max+1):
    if args.steps_can_repeat:
        plans += product(functions, repeat=step_num)
    else:
        plans += permutations(functions, step_num)


possible_outputs: Set[float] = set()
possible_steps: Dict[float, List[str]] = {}

for plan in plans:
    steps: List[str] = []
    n: float = args.starting_number
    for func in plan:
        n = func(n)
        steps.append(func.__name__)
    if args.ending_number is None:
        if n not in possible_outputs:
            possible_outputs.add(n)
            possible_steps[n] = steps
    elif n == args.ending_number:
        possible_steps[n] = steps
        break

if args.ending_number is None:
    print(possible_outputs)
else:
    print(possible_steps)
