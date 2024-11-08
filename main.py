from Fitur.sum import calculate_sum
from Fitur.difference import calculate_difference
from Fitur.product import calculate_product
from Fitur.divison import calculate_division

a = 10
b = 5
sum_result = calculate_sum(a,b)
difference_result = calculate_difference(a,b)
product_result = calculate_product(a,b)
division_result = calculate_division(a,b)

print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Division: {division_result}")