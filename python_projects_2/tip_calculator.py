# tip calculator


def calculate_tip(order_value, tip):
    try:
        order_value = float(order_value)
        tip = float(tip)
    except ValueError:
        print("Please enter a valid value")
        return None

    if order_value <= 0 or tip <= 0:
        print("Order value and tip must be positive values")
        return None

    tip_amount = (tip / 100) * order_value
    total_bill = order_value + tip_amount
    return tip_amount, total_bill


if __name__ == "__main__":
    order_value = input("What is value of your order (eg 152.95): ")
    tip = input("What percentage would you like to tip? ")
    if order_value and tip:
        tip_amount, total_bill = calculate_tip(order_value, tip)
    print(
        f"Your tip amount is {tip_amount:.2f}. Your total bill including tip is {total_bill:.2f}"
    )
