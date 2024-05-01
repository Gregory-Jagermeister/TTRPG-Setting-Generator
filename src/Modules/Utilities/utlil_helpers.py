import math

def process_duplicates(array):
    counts = {}
    processed_array = []

    for item in array:
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] += 1

    for key in counts:   
            processed_array.append(f"{key} (x{counts[key]})")

    return processed_array

def calc_cols(max_rows, array):
    return int(math.ceil(len(array) / max_rows))