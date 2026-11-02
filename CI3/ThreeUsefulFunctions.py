def find_max(numbers):
    """
    this fuction finds the maximum value in a list of numbers"""
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

def count_occurrences (items, target):
    """
    this function counts the number of occurences of target in items"""
    count = 0
    for item in items:
        if item == target:
            count+=1
    return count

def filter_by_value(d,minimum):
    """
    this functions return a dictionnary with only entries in d whose values are greater than minimum"""
    values_greater_than_min= {k:v for k,v in d.items() if v>minimum}
    return values_greater_than_min

print(find_max([4, 9, 2]))
print(count_occurrences(["a", "b", "a"], "a"))
print(filter_by_value( {"Ana": 15, "Ben": 9}, 10))