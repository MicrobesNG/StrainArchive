

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

        if str(strain_order["name"]) == str(selected_strain.name):

            present_in_basket = True

            strain_order["amount"] += 1
            strain_order["cost"] += selected_strain.cost

            break


    if not present_in_basket:

        orders.append(
            {"name": selected_strain.name, "amount": 1, "cost": selected_strain.cost}
        )
    
    request.session["basket"]["items"] = orders

    request.session.modified = True



def remove_from_basket(request, selected_strain):

    for strain_order in request.session["basket"]["items"]:

        if strain_order["name"] == selected_strain.name:

            if strain_order["amount"] > 1:

                strain_order["amount"] -= 1
                strain_order["cost"] -= selected_strain.cost
            
            elif strain_order["amount"] == 1:

                request.session["basket"]["items"].remove(strain_order)