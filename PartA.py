def total_combinations():
    die_a = [1, 2, 3, 4, 5, 6]
    die_b = [1, 2, 3, 4, 5, 6]
    return len(die_a) * len(die_b)


def distribution_combinations():
    die_a = [1, 2, 3, 4, 5, 6]
    die_b = [1, 2, 3, 4, 5, 6]
    distribution = [[0 for j in range(len(die_b))] for i in range(len(die_a))]

    for i in range(len(die_a)):
        for j in range(len(die_b)):
            sum_value = die_a[i] + die_b[j]
            distribution[i][j] = sum_value

    print("Distribution of all possible combinations:")
    for row in distribution:
        print(row)



def probability_sums():
    die_a = [1, 2, 3, 4, 5, 6]
    die_b = [1, 2, 3, 4, 5, 6]
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

    print("Probability of all possible sums:")
    for i in range(2, len(sum_counts) + 2):
        if(i<13):
            probability = sum_counts[i - 2] / total_combinations
            print(f"P(Sum = {i}) = {probability}")



print(f"Total number of combinations: {total_combinations()}\n\n")
distribution_combinations()
print("\n\n")
probability_sums()