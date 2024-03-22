from itertools import product

def undoom_dice(die_a, die_b):
    original_distribution = [[0 for j in range(len(die_b))] for i in range(len(die_a))]
    for i in range(len(die_a)):
        for j in range(len(die_b)):
            sum_value = die_a[i] + die_b[j]
            original_distribution[i][j] = sum_value

    sum_counts = [0] * (len(die_a) + len(die_b))
    for row in original_distribution:
        for value in row:
            sum_counts[value - 2] += 1

    original_sum_probabilities = [count / (len(die_a) * len(die_b)) for count in sum_counts]

    possible_combinations = []
    for combination in product(range(1, 11), repeat=6):
        if len(set(combination)) == 6:
            possible_combinations.append(list(combination))

    for combination in product(range(1, 7), repeat=6):
        new_die_a = list(combination[:6])
        new_die_b = list(combination[6:])
        new_sum_probabilities = calculate_sum_probabilities(new_die_a, new_die_b)
        if new_sum_probabilities == original_sum_probabilities:
            return new_die_a, new_die_b

    return None, None

def calculate_sum_probabilities(die_a, die_b):
    total_combinations = len(die_a) * len(die_b)
    distribution = [[0 for j in range(len(die_b))] for i in range(len(die_a))]

    for i in range(len(die_a)):
        for j in range(len(die_b)):
            sum_value = die_a[i] + die_b[j]
            distribution[i][j] = sum_value

    sum_counts = [0] * (len(die_a) + len(die_b))
    for row in distribution:
        for value in row:
            sum_counts[value - 2] += 1

    if total_combinations == 0:
        return [0] * len(sum_counts)

    sum_probabilities = [count / total_combinations for count in sum_counts]
    return sum_probabilities

die_a = [1, 2, 3, 4, 5, 6]
die_b = [1, 2, 3, 4, 5, 6]
new_die_a, new_die_b = undoom_dice(die_a, die_b)

if new_die_a and new_die_b:
    print("New Die A:", new_die_a)
    print("New Die B:", new_die_b)
    new_sum_probabilities = calculate_sum_probabilities(new_die_a, new_die_b)
    print("\nNew Sum Probabilities:")
    for i, p in enumerate(new_sum_probabilities, start=2):
        print(f"P(Sum = {i+2}) = {p}")
else:
    print("No solution found that maintains the original probability distribution.")