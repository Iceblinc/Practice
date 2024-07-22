import random


def find_pairs():
    first_value = random.randint(3, 20)
    print(f'Случайное число: {first_value}')

    pairs = []

    for i in range(1, first_value + 1):

        for j in range(i, first_value + 1):
            pair_sum = i + j

            if pair_sum != 0 and first_value % pair_sum == 0:
                pairs.append((i, j))

    return pairs


found_pairs = find_pairs()

fot_pairs = '|'.join(f'{i}-{j}' for i, j in found_pairs)
print(f'Найденая комбинацыя: {fot_pairs}')
