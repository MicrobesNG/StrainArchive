from . models import ConfirmedBasket

def save_session_basket_to_db(request):

    if request.session["basket"]:
        pass        
        # newBasket = ConfirmedBasket(

        # )

    else:

        raise AttributeError("Could not find basket in session.")





def get_basket(request):

    empty_basket = {
        "total_cost": 0.0,
        "items": []
    }
    
    if "basket" not in request.session:

        request.session["basket"] = empty_basket

    return request.session["basket"]


def add_to_basket(request, selected_strain):

    present_in_basket = False
    
    orders = request.session["basket"]["items"]
    
    for strain_order in orders:

        if strain_order["pk"] == selected_strain.pk:

            present_in_basket = True

            strain_order["amount"] += 1
            strain_order["cost"] += selected_strain.cost

            break


    if not present_in_basket:

        orders.append(
            {"name": selected_strain.name, "amount": 1, "cost": selected_strain.cost, "pk": selected_strain.pk}
        )
    

    request.session["basket"]["items"] = orders
    request.session.modified = True



def remove_from_basket(request, selected_strain):

    orders = request.session["basket"]["items"]

    for strain_order in orders:

        if strain_order["pk"] == selected_strain.pk:

            if strain_order["amount"] > 1:

                strain_order["amount"] -= 1
                strain_order["cost"] -= selected_strain.cost

            
            elif strain_order["amount"] == 1:
                
                orders.remove(strain_order)
                
    request.session["basket"]["items"] = orders
    request.session.modified = True



def calculate_basket_cost(request):

    return sum(item["cost"] for item in request.session["basket"]["items"])



def set_basket_cost(request):

    request.session["basket"]["total_cost"] = calculate_basket_cost(request)
    request.session.modified = True