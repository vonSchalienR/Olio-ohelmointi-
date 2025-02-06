def smallest_average(person1: dict, person2: dict, person3: dict):
    def avg(person):
        return (person["result1"] + person["result2"] + person["result3"]) / 3

    # Find the person with the smallest average
    smallest = min([person1, person2, person3], key=avg)
    
    return smallest

# Example usage:
person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

print(smallest_average(person1, person2, person3))
# Expected Output: {'name': 'Larry', 'result1': 3, 'result2': 1, 'result3': 1}
