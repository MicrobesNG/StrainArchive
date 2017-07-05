from . models import ConfirmedBasket, Purchase, Promotion, PromotionCode
import random, string
import json
from promotions import *


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

    # get the promotion
    promo = Promotion.objects.get(pk = promotion_pk)

    # get all the existing codes
    codes = [code.code for code in promo.promotioncode_set.all()]

    # create number of new codes
    for i in range(0, number_of_new_codes):

        # keep track of codes with the same code value
        already_in_use = True

        # assume new code is in use
        while already_in_use:
            
            # generate code
            new_code = generate_code(10)

            # if the code is unique append and break while loop
            if new_code not in codes:
                
                codes.append(new_code)

                already_in_use = False
            
            # if already present, repeat loop

        # once a unique code has been generated save to DB
        PromotionCode.objects.create(
            code = new_code,
            max_usages = max_uses_per_code,
            number_of_uses = 0,
            active = initially_active,
            promotion = promo
        )



# apply a promotional code to the session basket
def apply_code_to_session_basket(request, promotion_code):

    # get promotion parameters
    parameters = json.loads(promotion_code.promotion.promotion_parameters)

    # get session basket
    basket = request.session["basket"]

    # find promotion function and apply to basket
    PROMOTION_FUNCTION_MAP[promotion_code.promotion.promotion_type](request, parameters)

    # update the promotion code and save
    promotion_code.number_of_uses += 1
    promotion_code.save()