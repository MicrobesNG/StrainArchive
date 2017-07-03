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




def apply_code_to_session_basket(request, promocode_code):

    try:

        promotion_code = PromotionCode.objects.get(code = promocode_code)
    
    except PromotionCode.DoesNotExist:

        pass
    
    else:

        pass

        parameters = json.loads(promotion_code.promotion.promotion_type)

        