from santas_little_helpers.helpers import *
import re
from math import prod

input_data = read_input(19, numbers=False, separator='\n\n')

def parse_parts(in_data):
    return [{name: int(number) for name, number in re.findall(r'([a-z])=(\d+)', line)} for line in in_data]

def parse_workflows(in_data):
    workflows = {}
    for line in in_data:
        conditions = re.findall(r'\w.\d+:\w+', line)
        name, final_condition = re.findall(r'(\w+){.+,(\w+)}', line)[0]
        workflows[name] = (conditions, final_condition)
    return workflows

def calculate_workflows(part, workflows, current='in'):
    x = part['x']
    m = part['m']
    a = part['a']
    s = part['s']
    while True:
        conditions, final_goto = workflows[current]
        for cr in conditions:
            condition, goto = cr.split(':')
            if eval(condition):
                current = goto
                break
            else:
                current = final_goto
        if current == 'A':
            return sum(part.values())
        if current == 'R':
            return 0

def apply_condition_to_range(condition: str, in_range: range) -> tuple:
    condition_sign = condition[1]
    condition_number = int(condition[2:])
    if condition_sign == '>':
        satisfies = (condition_number+1, in_range[1])
        not_satisfies = (in_range[0], condition_number)
    else:
        satisfies = (in_range[0], condition_number-1)
        not_satisfies = (condition_number, in_range[1])
    
    return satisfies, not_satisfies

def find_all_accepted_combinations(part_ranges, workflows, current='in'):
    result = 0
    # exit conditions
    if current == 'A':
        # accepted workflow: calculate all combos (multiply range lengths)
        return prod(r[1] - r[0]+1 for r in part_ranges.values() if r[1] > r[0])
    if current == 'R':
        # rejected
        return 0
    
    # we haven't reached A or R
    conditions, default = workflows[current]

    for cr in conditions:
        condition, goto = cr.split(':')
        letter = condition[0]
        satisfies, not_satisfies = apply_condition_to_range(condition, part_ranges[letter])
        # satisfies -> we move forward with this range to the next part:
        part_ranges = {l: v for l,v in part_ranges.items()}
        part_ranges[letter] = satisfies
        result += find_all_accepted_combinations(part_ranges, workflows, goto)
        # we do the same thing again, but save the not_satisfies ranges so next time
        # we enter the loop the previous letter range will already be updated
        part_ranges = {l: v for l,v in part_ranges.items()}
        part_ranges[letter] = not_satisfies
    # this is the default, applied to "not satisy" ranges after standard conditions have been applied
    result += find_all_accepted_combinations(part_ranges, workflows, default)

    return result



parts = parse_parts(input_data[1].split('\n'))
workflows = parse_workflows(input_data[0].split('\n'))
party_1 = sum(calculate_workflows(part, workflows) for part in parts)

part_ranges = {c: (1, 4000) for c in 'xmas'}
party_2 = find_all_accepted_combinations(part_ranges, workflows, 'in')

print_solutions(party_1, party_2)


def test_one():
    assert party_1 == 398527

def test_two():
    assert party_2 == 133973513090020
