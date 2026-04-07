
def find_max(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

print(find_max([1, 2, 3, 4, 5]))

def find_min(arr):
    min_value = arr[0]
    for num in arr:
        if num < min_value:
            min_value = num
    return min_value

print(find_min([1, 2, 3, 4, 5]))

def find_average(arr):
    total = 0
    for num in arr:
        total += num
    return total / len(arr)

print(find_average([1, 2, 3, 4, 5]))

def find_median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2
    else:
        return sorted_arr[n//2]
    
print(find_median([1, 2, 3, 4, 5]))

def find_mode(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    max_count = max(count_dict.values())
    mode = [k for k, v in count_dict.items() if v == max_count]
    return mode

print(find_mode([1, 2, 2, 3, 3, 3]))

def find_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

print(find_sum([1, 2, 3, 4, 5]))


def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))