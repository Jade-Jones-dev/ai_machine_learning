# tip calculator

def calculate_tip(order_value, tip):
    order_value = float(order_value)
    tip = float(tip)
    tip_amount = (order_value / 100) * tip
    total_bill = order_value + tip_amount
    print(
        f"Your tip amount is {tip_amount:.2f}. Your total bill including tip is {total_bill:.2f}"
    )


if __name__ == "__main__":
    order_value = input("What is value of your order (eg 152.95): ")
    tip = input("What percentage would you like to tip? ")
    calculate_tip(order_value, tip)
