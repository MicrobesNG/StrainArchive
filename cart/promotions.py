

def apply_fixed_price_reduction(basket, amount):

    # apply reduction and set promotion total cost to new amount
    basket["promotion"]["promotion_total_cost"] = basket["total_cost"] - amount

    # clamp the cost to be greater than or equal to 0
    if basket["promotion"]["promotion_total_cost"] < 0:
        basket["promotion"]["promotion_total_cost"] = 0.0



def apply_percentage_price_reduction(basket, percentage):

    # calculate percentage of amount
    percentage_amount = (basket['total_cost']/100) * percentage

    # reduce total cost by percentage
    basket["promotion"]["promotion_total_cost"] = basket["total_cost"] - percentage_amount




# map to store functions
# lets functions be called by dict key
PROMOTION_FUNCTION_MAP = {
    "FPR": apply_fixed_price_reduction,
    "PPR": apply_percentage_price_reduction
}