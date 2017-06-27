from . models import ConfirmedBasket, Purchase, Promotion, PromotionCode
from archive.models import Strain
import random, string



# generates random string
def generate_code(length):

    return ''.join(random.choice(string.lowercase) for i in range(length)).upper()



# generates codes for promotion
def generate_codes_for_promotion(
        promotion_pk,
        number_of_new_codes,
        max_uses_per_code,
        initially_active
    ):
    promo = Promotion.objects.get(pk = promotion_pk)

    codes = [code.code for code in promo.promotioncode_set.all()]

    for i in range(0, number_of_new_codes):

        already_in_use = True

        while already_in_use:
            
            new_code = generate_code(10)

            if new_code not in codes:
                
                codes.append(new_code)

                already_in_use = False

        PromotionCode.objects.create(
            code = new_code,
            max_usages = max_uses_per_code,
            number_of_uses = 0,
            active = initially_active,
            promotion = promo
        )



# creates basket in the DB based on session basket
def save_session_basket_to_db(request):

    if request.session["basket"]:

        session_basket = request.session["basket"]

        newBasket = ConfirmedBasket.objects.create(
            total_cost = session_basket["total_cost"]
        )

        for item in session_basket["items"]:

            newPurchase = Purchase.objects.create(
                strain = Strain.objects.get(pk = int(item["pk"])),
                quantity = item["amount"],
                cost = item["cost"]
            )

            newBasket.purchases.add(newPurchase)
        
        newBasket.save()

        return newBasket

    else:

        raise AttributeError("Could not find basket in session.")



# gets empty basket or session basket if present
def get_basket(request):

    empty_basket = {
        "total_cost": 0.0,
        "items": []
    }
    
    if "basket" not in request.session:

        request.session["basket"] = empty_basket

    return request.session["basket"]





def apply_code_to_session_basket(request, promocode_code):

    pass






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
            {"name": selected_strain.name, "amount": 1, "cost": selected_strain.cost, "pk": selected_strain.pk}
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