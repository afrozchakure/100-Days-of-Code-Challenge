from itertools import combinations
def print_powerset(string):
    for i in range(0, len(string) + 1):
        for element in combinations(string, i):
            print(''.join(element))
string = ['a', 'b', 'c']
print_powerset(string)

