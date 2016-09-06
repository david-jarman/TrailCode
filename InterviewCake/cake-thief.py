def max_duffel_bag_value(cake_tuples, max_capacity):
    max_duffel_bag_values = [0] * (max_capacity + 1)

    for capacity in range(max_capacity + 1):
        for cake_weight, cake_value in cake_tuples:
            if cake_weight == 0 and cake_value > 0:
                return float('inf')
            if cake_weight > capacity:
                continue
            elif cake_weight == capacity:
                max_duffel_bag_values[capacity] = max(max_duffel_bag_values[capacity], cake_value)
            else:
                max_1 = cake_value
                max_2 = max_duffel_bag_values[capacity - cake_weight]
                max_duffel_bag_values[capacity] = max(max_duffel_bag_values[capacity], max_1 + max_2)

    return max_duffel_bag_values[max_capacity]

print max_duffel_bag_value([(7, 160), (3, 90), (2, 15), (1,1)], 20)
