

def get_basket(request):
    empty_basket = {
        "total_cost": 0.0,
        "items": []
    }
    
    if "basket" in request.session:

        if request.session["basket"] != empty_basket:

            basket = request.session["basket"]
        
        else:

            basket = empty_basket
    
    else:

        basket = empty_basket
    

    return basket


def add_to_basket(request, selected_strain):
    
    present_in_basket = False
    for strain_order in request.session["basket"]["items"]:

        if strain_order["name"] == selected_strain.name:

            present_in_basket = True

            strain_order["amount"] += 1
            strain_order["cost"] += selected_strain.cost

    if not present_in_basket:

        request.session["basket"]["items"].append(
            {"name": selected_strain.name, "amount": 1, "cost": selected_strain.cost}
        )


def remove_from_basket(request, selected_strain):

    for strain_order in request.session["basket"]["items"]:

        if strain_order["name"] == selected_strain.name:

            if strain_order["amount"] > 1:

                strain_order["amount"] -= 1
                strain_order["cost"] -= selected_strain.cost
            
            elif strain_order["amount"] == 1:

                request.session["basket"]["items"].remove(strain_order)