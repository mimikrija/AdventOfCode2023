from santas_little_helpers.helpers import *
import re

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
            return True
        if current == 'R':
            return False

def get_rating(part):
    return sum(part.values())

parts = parse_parts(input_data[1].split('\n'))
workflows = parse_workflows(input_data[0].split('\n'))

party_1 = sum(get_rating(part) for part in parts if calculate_workflows(part, workflows))
print_solutions(party_1)

def test_one():
    assert party_1 == 398527
