from santas_little_helpers.helpers import *
from collections import deque, defaultdict


input_data = read_input(20)

def parse_input(input_data):
    flip_flops = {}
    conjunctions = {}
    broadcasters = set()
    connections = {}
    for line in input_data:
        left, right = line.split(' -> ')
        typ = left[0]
        source = left[1:]
        destinations = right.split(', ')
        if left == 'broadcaster':
            broadcasters.add(left)
            connections[left] = destinations
        elif typ == '%':
            flip_flops[source] = ('off', 'low')
            connections[source] = destinations
        elif typ == '&':
            conjunctions[source] = 'low'
            connections[source] = destinations
    return connections, flip_flops, conjunctions, broadcasters

def push_the_button(module_configuration, count=1000):
    connections, flip_flops, conjunctions, broadcasters = module_configuration
    lows = 0
    highs = 0

    for _ in range(count):
        modules = deque([('broadcaster', 'low')])
        while modules:
            current, signal = modules.popleft()
            if signal == 'high':
                highs +=1
            else:
                lows += 1
            #print(f'highs: {highs}, lows: {lows}')
            if current not in connections:
                continue
            destinations = connections[current]

            if current in broadcasters:
                new_signal = signal
            elif current in flip_flops:
                if flip_flops[current][0] == 'off' and signal == 'low':
                    flip_flops[current] = ('on', 'high')
                    new_signal = 'high'
                elif flip_flops[current][0] == 'on' and signal == 'low':
                    flip_flops[current] = ('off', 'low')
                    new_signal = 'low'
                # If a flip-flop module receives a high pulse, it is ignored and nothing
                else:
                    continue
            elif current in conjunctions:
                from_flip_flops = all(flip_flops[source][1]=='high' for source, dest in connections.items() if current in dest and source in flip_flops and source in connections)
                from_conjunctions = all(conjunctions[source]=='high' for source, dest in connections.items() if current in dest and source in conjunctions and source in connections)
                if from_flip_flops and from_conjunctions:
                    new_signal = "low"
                else:
                    new_signal = "high"

            for destination in destinations:
                modules.append((destination, new_signal))

    print(f'total highs: {highs}')
    print(f'total lows: {lows}')
    return highs*lows


module_configuration = parse_input(input_data)


party_1 = push_the_button(module_configuration)
print_solutions(party_1)
# 510258078 too low
# 573656292 too low