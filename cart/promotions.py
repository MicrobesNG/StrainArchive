
def apply_free_strains(basket, numer_of_free_strains):

    reduction_in_cost = 0




def apply_fixed_price_reduction(request, parameters):
    
    basket = request.session["basket"]

    # get amount
    amount = parameters["reduction_amount"]

    # apply reduction and set promotion total cost to new amount
    basket["promotion"]["promotion_total_cost"] = basket["total_cost"] - amount

    # clamp the cost to be greater than or equal to 0
    if basket["promotion"]["promotion_total_cost"] < 0:
        basket["promotion"]["promotion_total_cost"] = 0.0
    
    request.session.modified = True



def apply_percentage_price_reduction(request, parameters):
    
    basket = request.session["basket"]
    
    # get percentage
    percentage_amount = parameters["percentage_reduction"]

    # calculate percentage of amount
    percentage_amount = (basket['total_cost']/100) * percentage

    # reduce total cost by percentage
    basket["promotion"]["promotion_total_cost"] = basket["total_cost"] - percentage_amount

    request.session.modified = True




# map to store functions
# lets functions be called by dict key
PROMOTION_FUNCTION_MAP = {
    "FPR": apply_fixed_price_reduction,
    "PPR": apply_percentage_price_reduction,
    "FS": apply_free_strains
}