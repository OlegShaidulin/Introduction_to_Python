def calculate_structure_sum(data_structure):
    amount = 0
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            amount += calculate_structure_sum(key)
            amount += calculate_structure_sum(value)
    elif isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            amount +=calculate_structure_sum(i)
    elif isinstance(data_structure, (int, float)):
        amount += data_structure
    elif isinstance(data_structure, str):
        amount += len(data_structure)
    return amount

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))