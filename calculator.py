from itertools import permutations, product
from typing import Dict, List, Any, Optional, Set

from calculator_functions import functions


# argparse, func
# Start parameters:
step_min: int = 1
step_max: int = 2
steps_can_repeat = True
starting_number: float = 1
ending_number: Optional[float] = None

assert step_max >= step_min, "step_max must not be smaller than step_min"
assert steps_can_repeat or step_min <= len(functions), "repeat off - few steps"

plans: List[Any] = []
for step_num in range(step_min, step_max+1):
    if steps_can_repeat:
        plans += product(functions, repeat=step_num)
    else:
        plans += permutations(functions, step_num)


possible_outputs: Set[float] = set()
possible_steps: Dict[float, List[str]] = {}

for plan in plans:
    steps: List[str] = []
    n: float = starting_number
    for func in plan:
        n = func(n)
        steps.append(func.__name__)
    if ending_number is None:
        if n not in possible_outputs:
            possible_outputs.add(n)
            possible_steps[n] = steps
    elif n == ending_number:
        possible_steps[n] = steps

print(possible_outputs)
