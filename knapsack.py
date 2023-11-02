class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.value_per_weight = value / weight

def knapsack_fractional(items, capacity):
    items.sort(key=lambda item: item.value_per_weight, reverse=True)
    total_value = 0
    knapsack = []

    for item in items:
        if capacity == 0:
            break
        
        weight_to_take = min(item.weight, capacity)
        total_value += weight_to_take * item.value_per_weight
        capacity -= weight_to_take
        knapsack.append((item, weight_to_take))

    return total_value, knapsack

def main():
    n = int(input("Enter the number of items: "))
    items = []

    for i in range(n):
        weight, value = map(int, input(f"Enter weight and value for item {i+1}: ").split())
        items.append(Item(weight, value))

    capacity = int(input("Enter the knapsack capacity: "))

    total_value, knapsack = knapsack_fractional(items, capacity)

    print("Knapsack items and their fractions:")
    for item, fraction in knapsack:
        print(f"Item with weight {item.weight}, value {item.value}: Fraction taken = {fraction}")

    print("Total value in knapsack:", total_value)
if __name__ == "__main__":
    main()

# Enter the number of items: 6
# Enter weight and value for item 1: 10 80
# Enter weight and value for item 2: 20 120
# Enter weight and value for item 3: 30 100
# Enter weight and value for item 4: 40 200
# Enter weight and value for item 5: 50 150
# Enter weight and value for item 6: 60 170
# Enter the knapsack capacity: 150
# Knapsack items and their fractions:
# Item with weight 10, value 80: Fraction taken = 10
# Item with weight 20, value 120: Fraction taken = 20
# Item with weight 40, value 200: Fraction taken = 40
# Item with weight 30, value 100: Fraction taken = 30
# Item with weight 50, value 150: Fraction taken = 50
# Total value in knapsack: 650.0