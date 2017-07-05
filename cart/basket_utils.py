from . models import ConfirmedBasket, Purchase, Promotion, PromotionCode
from archive.models import Strain




# creates basket in the DB based on session basket
def save_session_basket_to_db(request):

    if request.session["basket"]:

        session_basket = request.session["basket"]

        new_basket = ConfirmedBasket.objects.create(
            total_cost = session_basket["total_cost"]
        )

        try:
        
            applied_promotion = Promotion.objects.get(pk = session_basket["promotion"]["promotion_pk"])
        
        except Promotion.DoesNotExist:
            
            print "PROMO NOT FOUND"

        else:

            new_basket.applied_promotion = applied_promotion
            new_basket.promotion_cost = session_basket["promotion"]["promotion_total_cost"]

        try:

            applied_promotion_code = PromotionCode.objects.get(code = session_basket["promotion"]["promotion_code"])
        
        except PromotionCode.DoesNotExist:

            print "CODE NOT FOUND"
        
        else:

            new_basket.applied_code = applied_promotion_code

        for item in session_basket["items"]:

            newPurchase = Purchase.objects.create(
                strain = Strain.objects.get(pk = int(item["pk"])),
                quantity = item["amount"],
                cost = item["cost"]
            )

            new_basket.purchases.add(newPurchase)
        
        new_basket.save()

        return new_basket

    else:

        raise AttributeError("Could not find basket in session.")

# returns empty basket
def generate_empty_basket():

    empty_basket = {
        "total_cost": 0.0,
        "items": [],
        "promotion": {
            "promotion_code": "",
            "promotion_pk": "",
            "promotion_description": "",
            "promotion_total_cost": 0.0
        }
    }

    return empty_basket



# gets empty basket or session basket if present
def get_basket(request):

    empty_basket = {
        "total_cost": 0.0,
        "items": [],
        "promotion": {
            "promotion_code": "",
            "promotion_pk": "",
            "promotion_total_cost": 0.0
        }
    }
    
    if "basket" not in request.session:

        request.session["basket"] = empty_basket

    return request.session["basket"]



# adds an item to the basket
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
            {
                "name": selected_strain.name,
                "amount": 1,
                "cost": selected_strain.cost,
                "pk": selected_strain.pk
            }
        )
    

    request.session["basket"]["items"] = orders
    request.session.modified = True


# removes an item from the basket
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



# returns total cost by summing each purchase cost
def calculate_basket_cost(request):

    return sum(item["cost"] for item in request.session["basket"]["items"])


# sets the total cost of the basked based on calculated basket cost
def set_basket_cost(request):

    request.session["basket"]["total_cost"] = calculate_basket_cost(request)
    request.session.modified = True