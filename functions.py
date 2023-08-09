print("Hello World! It feels good to be back!")

zubi_expences = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
zabi_expences = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]

def calculate_total_expences(expences):
    total_expences = 0
    for expence in expences:
        total_expences += expence
    return total_expences

print("Zubi's total expences are: ", calculate_total_expences(zubi_expences))
print("Zabi's total expences are: ", calculate_total_expences(zabi_expences))