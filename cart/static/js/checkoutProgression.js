
var CHECKOUT_FRAMES = [
    "paymentDetailsTab",
    "addressTab",
    "promotionsTab",
    "notesTab"
];

function validatePaymentDetails() {

    return true;

}


$(document).ready(function() {

    $(".nextButton").click(function() {
        if (validatePaymentDetails) {
            
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