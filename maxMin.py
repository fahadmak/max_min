def find_max_min(data):
    min_max = []
    seq = sorted(data)
    numbers =len(seq)
    min = seq[0]
    max = seq[- 1]
    for i in seq:
        if min == max:
            min_max.append(numbers)
            return min_max
        else:
            min_max.append(min)
            min_max.append(max)
            return min_max
