import itertools

truthtable = [
    ([0, 0, 1, 1], 1),
    ([0, 0, 1, 0], 0),
    ([0, 1, 1, 1], 0),
]

def calc_f(w, x, y, z):
    return ((not x or y) or (z == x)) and (not w or z)

for perm in itertools.permutations(range(4)):
    valid = True
    for row, expected in truthtable:
        w, x, y, z = [row[i] for i in perm]
        if calc_f(w, x, y, z) != expected:
            valid = False
            break
    if valid:
        variable_names = ['w', 'x', 'y', 'z']
        result = [''] * 4
        for var, idx in zip(variable_names, perm):
            result[idx] = var
        answer = ''.join(result)
        print("ответ:", answer)
        break
