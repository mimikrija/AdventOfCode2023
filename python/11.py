from santas_little_helpers.helpers import *
from itertools import combinations


def get_columns_rows(coords):
    columns, rows = (sorted({c[p] for c in coords}) for p in (0,1))
    return columns, rows

def expand(rowcol, factor=2):
    rc = {r: r for r in rowcol}
    diff = 0
    for l, r in zip(rowcol, rowcol[1:]):
        diff += (r-l-1)*(factor-1)
        rc[r] += diff
    return rc

def expand_universe(galaxies, factor):
    columns, rows = get_columns_rows(galaxies)
    excolumns, exrows = (expand(rc, factor) for rc in (columns, rows))
    return {(excolumns[x], exrows[y]) for x, y in galaxies}


input_data = read_input(11)

galaxies = {(x, y) for y, row in enumerate(input_data) for x, c in enumerate(row) if c=='#'}

party_1, party_2 = (sum(manhattan(first, second)
                        for first, second in combinations(expand_universe(galaxies, factor), r=2))
                        for factor in (2, 1000000))

print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 9639160

def test_two():
    assert party_2 == 752936133304
