from santas_little_helpers.helpers import *
from collections import defaultdict, namedtuple
from dataclasses import dataclass
from itertools import product


Corner = namedtuple('Corner', 'x,y,z')
Cell = namedtuple('Cell', 'x,y')

@dataclass
class Slab:
    id: int
    min_z: int
    height: int
    installed_z: int
    supported_by = set()
    projection = set()
    
    def set_projection(self, projection):
        self.projection = projection
    
    def calculate_supports(self, other):
        if self.projection & other.projection:
            if self.installed_z == other.installed_z + other.height:
                self.supported_by = self.supported_by.copy()
                self.supported_by.add(other.id)
    
    def __eq__(self, other) -> bool:
        return self.installed_z == other.installed_z and self.projection == other.projection




def parse_slabs(input_data):
    slabs = list()
    for id, line in enumerate(input_data):
        begin, end = line.split('~')
        begin = Corner(*(int(c) for c in begin.split(',')))
        end = Corner(*(int(c) for c in end.split(',')))
        projection = set((x, y) for x in range(begin.x, end.x + 1) for y in range(begin.y, end.y+1))
        height = abs(end.z - begin.z) + 1
        lowest_z = min(end.z, begin.z)
        slab = Slab( id, lowest_z, height, None)
        slab.set_projection(projection)
        slabs.append(slab)
    # return slabs sorted by closest to the ground
    return sorted(slabs, key=lambda slab: slab.min_z)

def find_supports(consolidated):
    for below, above in product(consolidated, repeat=2):
        above.calculate_supports(below)





def consolidate(slabs):
    surface = defaultdict(int)
    consolidated = []
    for slab in slabs:
        available_Z = max(surface[xy] for xy in slab.projection)
        #print(f'{slab.id} surface before falling: \n  {surface}, \n max available z: {available_Z}')
        slab.installed_z = available_Z + 1
        for xy in slab.projection:
            surface[xy] = available_Z + slab.height
        consolidated.append(slab)
    return consolidated

def how_many_can_go_out(slabs):
    consolidated = consolidate(slabs)
    single_slab_supports = set()
    for slab in slabs:
        if len(slab.supported_by) == 1:
            single_slab_supports.add(slab.supported_by.pop())
    return len(consolidated) - len(single_slab_supports)

input_data = read_input(22)
slabs = parse_slabs(input_data)

conso = consolidate(slabs)




find_supports(conso)


party_1 = how_many_can_go_out(slabs)



print_solutions(party_1)

def test_one():
    assert party_1 == 517
