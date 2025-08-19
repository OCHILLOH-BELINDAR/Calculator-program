def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or more, apply it. Otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input
price_input = float(input("Enter the original price of the item: "))
discount_input = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price_input, discount_input)

# Display the result
if discount_input >= 20:
    print(f"Discount applied. Final price: ${final_price:.2f}")
else:
    print(f"No discount applied. Final price: ${final_price:.2f}")



