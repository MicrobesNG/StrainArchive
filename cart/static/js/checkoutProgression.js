
$(document).ready(function() {

    $(".nextButton").click(function() {
        
        var moveNext = false;

        if ($(this).attr("id") == "paymentNext") {
            if (validatePaymentDetails()) {
                moveNext = true;
            }
        } else if ($(this).attr("id") == "billingNext") {
            if (validateBillingAddressDetails()) {
                moveNext = true;
            }
        } else if ($(this).attr("id") == "deliveryNext") {
            if (validateDeliveryAddressDetails()) {
                moveNext = true;
            }
        } else {
            moveNext = true;
        }

        if (moveNext) {
            
            var currentID = $(this).parents(".tab-pane").attr("id");
            
            var nextId = $(this).parents('.tab-pane').next().attr("id");
            
            $('[href="#'+nextId+'"]').addClass("activeSelector");
            $('[href="#'+nextId+'"]').tab('show');
            
            $('[href="#'+currentID+'"]').removeClass("activeSelector");
            $('[href="#'+currentID+'"]').addClass("completeSelector");


        } else {
            // display an error modal
        }

    });

});