# Create a function named calculate_discount that takes two parameters:

# price: The original price of an item (float)
# discount_percentage: The discount percentage (float)
# The function should:

# Calculate the discount amount
# Subtract the discount amount from the original price
# Round the result to 2 decimal places
# Return the final discounted price
# For example, if the original price is $100 and the discount is 20%, the function should return $80.00.

def calculate_discount(price, discount_percentage):
  discount = float(price) * float(discount_percentage) / 100
  calc_with_discount = price - discount
  return round(calc_with_discount, 2)

print(calculate_discount(75.5, 10))
print(calculate_discount(349.99, 25.5))