from santas_little_helpers.helpers import *
from collections import deque, defaultdict
from math import prod
from dataclasses import dataclass

@dataclass
class Module:
    name: str
    send_to: list[str]

    def build_pulses(self, source, pulse_type):
        return [(self.name, pulse_type, s) for s in self.send_to]

@dataclass
class FlipFlopModule(Module):
    state = False # all flipflops start as off

    def send(self, source, pulse_type):
        if pulse_type == 'high':
            return []
        if self.state:
            send_pulse = 'low'
        else:
            send_pulse = 'high'
        self.state = not self.state
        return self.build_pulses(source, send_pulse)

@dataclass
class ConjunctionModule(Module):
    sources: dict

    def send(self, source, pulse_type):
        self.sources[source] = pulse_type
        if all(s == 'high' for s in self.sources.values()):
            send_pulse = 'low'
        else:
            send_pulse = 'high'
        return self.build_pulses(source, send_pulse)

@dataclass
class BroadcasterModule(Module):
    def send(self, source, pulse_type):
        return self.build_pulses(source, 'low')





input_data = read_input(20)

def parse_input(input_data):
    modules = {}
    conjunctions = set()
    for line in input_data:
        left, right = line.split(' -> ')
        typ = left[0]
        name = left[1:]
        destinations = right.split(', ')
        match(typ):
            case 'b':
                modules['broadcaster'] = (BroadcasterModule('broadcaster', destinations))
            case '%':
                modules[name] = FlipFlopModule(name, destinations)
            case '&':
                modules[name] = ConjunctionModule(name, destinations, dict())
                conjunctions.add(name)
    conjunctions_sources = defaultdict(list)
    for module_name, module in modules.items():
        for d in module.send_to:
            if d in conjunctions:
                conjunctions_sources[d].append(module.name)
    
    for module in modules.values():
        if isinstance(module, ConjunctionModule):
            module.sources = {name: 'low' for name in conjunctions_sources[module.name]}

    return modules


def push_the_button(modules, count=1000):
    total = defaultdict(int)
    
    for _ in range(count):
        total['low'] += 1 #button
        for module in modules.values():
            if isinstance(module, BroadcasterModule):
                to_solve = deque(module.send('', 'low'))
        while to_solve:
            source, pulse_type, destination = to_solve.popleft()
            total[pulse_type] += 1
            if destination not in modules:
                continue
            to_solve += modules[destination].send(source, pulse_type)


    print(f'totals: {total}')

    return prod(total.values())


def find_the_count(modules):
    solutions = []    
    test = ['dr', 'tn', 'bm', 'cl']
    button_press = 0
    print(f'analyzing {test}')

    while True:
        button_press += 1 #button
        for module in modules.values():
            if isinstance(module, BroadcasterModule):
                to_solve = deque(module.send('', 'low'))
        while to_solve:
            source, pulse_type, destination = to_solve.popleft()
            if destination not in modules:
                continue
            if destination in test and pulse_type == 'low':
                solutions.append(button_press)
            if len(solutions) == len(test):
                return prod(solutions)
            to_solve += modules[destination].send(source, pulse_type)


module_configuration1 = parse_input(input_data)
module_configuration2 = parse_input(input_data)

party_1 = push_the_button(module_configuration1)
party_2 = find_the_count(module_configuration2)


print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 747304011

def test_two():
    assert party_2 == 220366255099387
